from ice.api import API
from ice.engine import Engine, build

INTERVAL = 60

# Temporary configuration
CONFIG = {
  "systems": [
    {"name": "system_1"},
    {"name": "system_2"}
  ],

  "capabilities": [
    {
      "name": "cap_1",
      "src": "system_1",
      "dst": "system_2",
      "origin": "dst",
      "check": "cap_1_check"
    },
    {
      "name": "cap_2",
      "src": "system_1",
      "dst": "system_2",
      "state": True
    }
  ],

  "requirements": [
    {
      "name": "requirement_1",
      "src": "system_2",
      "contract": "cap_1 or cap_2"
    }
  ]
}

def main():
    # Start API
    api = API()
    engine = Engine(INTERVAL)

    while True:
        # Get systems and probes
        systems, probes = build(CONFIG) # API config input blocks once implemented
        if not engine.reload(systems, probes):
            # Failure, invoke API response
            break

if __name__ == "__main__":
    main()