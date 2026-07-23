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

def line(level, r):
    return json.dumps({
        "timestamp": time.time(),
        "level": level,
        "message": f"{r.name}: {level.lower()}",
        "requirement": r.name,
        "src": r.src.name,
        "trace": render(r.contract),
    })

def resolution(r):
    return line("OK", r)

def violation(r):
    return line("VIOLATED", r)

def error(r):
    return line("UNRESOLVED", r)

def rejection(r):
    return line("BLOCKING", r)