from ice.api import API
from ice.engine.builder import build
from ice.engine import Engine

INTERVAL = 60

def main():

    api = API()
    engine = Engine(INTERVAL)
    
    while True:

        # Get systems and probes
        config = api.listen()
        systems = build(config)
        passes, fails, errors = engine.reload(systems)
        api.respond(passes, fails, errors)

if __name__ == "__main__":
    main()