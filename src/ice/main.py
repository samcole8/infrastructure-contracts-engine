from ice.api import API
from ice.engine import Engine

INTERVAL = 60


def main():
    api = API()
    engine = Engine(INTERVAL)
    engine.start()

if __name__ == "__main__":
    main()