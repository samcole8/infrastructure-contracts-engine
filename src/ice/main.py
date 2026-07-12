import threading

from ice.engine import Engine
from ice.system import System

INTERVAL=60

def main():
    engine = Engine(interval=INTERVAL)
    threading.Thread(target=engine.listen, daemon=True).start()
    engine.start()

if __name__ == "__main__":
    main()