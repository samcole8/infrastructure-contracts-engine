def resolution(r):
    return f"RESOLUTION: {r.name}       (Requirement has entered a fulfilled state)"

def rejection(r):
    return f"REJECTION: {r.name}        (Requirement depends on capabilities that are declared and either violated or errored)"

def violation(r):
    return f"VIOLATION: {r.name}        (Requirement has entered a violated state)"

def error(r):
    return f"ERROR: {r.name}            (Requirement could not be evaluated due to errors)"
