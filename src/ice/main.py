from ice.api import API
from ice.engine.builder import build
from ice.engine import Engine
from ice.reporting import terraform

INTERVAL = 60

def main():

    api = API()
    engine = Engine(INTERVAL)
    
    while True:

        # Get systems and probes
        config = api.listen()
        systems = build(config)
        errors = engine.reload(systems)
        if errors:
            api.respond(terraform.response(errors))
        else:
            api.respond(None)

if __name__ == "__main__":
    main()