import json, time

from ice.model import Capability, And, Or, Not

def render(node):
    if isinstance(node, Capability):
        return f"({node.name}:={node.state})"
    if isinstance(node, And):
        return "(" + " and ".join(render(o) for o in node.operands) + ")"
    if isinstance(node, Or):
        return "(" + " or ".join(render(o) for o in node.operands) + ")"
    if isinstance(node, Not):
        return f"not {render(node.operand)}"

def line(status, r):
    return json.dumps({
        "timestamp": time.time(),
        "status": status,
        "message": f"{r.name}: {status.lower()}",
        "requirement": r.name,
        "system": r.src.name,
        "trace": render(r.contract),
    })

def pass_jsonl(r):
    return line("PASS", r)

def fail_jsonl(r):
    return line("FAIL", r)

def error_jsonl(r):
    return line("ERROR", r)

# def rejection(r):
#     return line("BLOCKING", r)