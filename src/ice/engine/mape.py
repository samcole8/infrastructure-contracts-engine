from ice.reporting import report

def monitor(systems):
    mod_requirements = set()
    for s in systems:
        mod_requirements |= s.poll()
    return mod_requirements

def analyse(mod_requirements):
    # Analyse / Plan

    passes = []
    fails = []
    errors = []

    # rejections = []
    for r in mod_requirements:
        result = r.evaluate()
        if result is True:
            passes.append(report.pass_jsonl(r))
        elif result is False:
            fails.append(report.fail_jsonl(r))
        elif result is None:
            errors.append(report.error(r))

    return passes, fails, errors

def tick(systems):
    print("EXECUTING")
    mod_requirements = monitor(systems)
    passes, fails, errors = analyse(mod_requirements)
    return passes, fails, errors
