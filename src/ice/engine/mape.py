from ice.reporting import report

def monitor(systems):
    mod_requirements = set()
    for s in systems:
        mod_requirements |= s.poll()
    return mod_requirements

def analyse_and_plan(mod_requirements):
    # Analyse / Plan

    resolutions = []
    violations = []
    errors = []
    rejections = []
    for r in mod_requirements:
        result = r.evaluate()

        if result is True:
            resolutions.append(r)
        elif result is False:
            violations.append(r)
        elif result is None:
            errors.append(r)

        if result is not True and r.has_static_capabilities:
            rejections.append(r)

    return resolutions, violations, errors, rejections

def execute(resolutions, violations, errors, rejections):
    for r in resolutions:
        print(report.resolution(r))

    for r in violations:
        print(report.violation(r))

    for r in errors:
        print(report.error(r))

    rejection_messages = []
    for r in rejections:
        message = report.rejection(r)
        print(message)
        rejection_messages.append(message)

    if len(rejection_messages) == 0:
        rejection_messages = None
    return rejection_messages


def tick(systems):
    print("EXECUTING")
    mod_requirements = monitor(systems)
    resolutions, violations, errors, rejections = analyse_and_plan(mod_requirements)
    errors = execute(resolutions, violations, errors, rejections)
    return errors
