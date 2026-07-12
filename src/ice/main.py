import threading
from time import sleep

INTERVAL=60

class System:

    def __init__(self, name, username=None, password=None):
        self.name = name
        self.username = username
        self.password = password

class Capability:
    def __init__(self, system):
        self.system = system

class Contract:
    def __init__(self, src, dst, expression):
        self.src = src
        self.dst = dst
        self.expression = expression
    
    def evaluate(self):
        return self.expression(self.src, self.dst)

class Engine:

    def __init__(self):
        self._knowledge_cache = None
        self.contracts = []
    
    def _monitor(self):
        # Run capability checks
        pass

    def _analyse(self):
        # Evaluate contracts
        pass

    def _plan(self):
        # Decide what to do about violations if they occur, add tasks to queue
        pass

    def _execute(self):
        # Respond to violations in queue
        pass

    def _knowledge(self):
        # Update knowledge base
        if self._knowledge_cache:
            self.contracts = self._knowledge_cache
            self._knowledge_cache = None

    def listen(self):
        # Start input API
        sleep(0.1)

    def start(self):
        # Start MAPE loop
        while True:
            self._monitor()
            self._analyse()
            self._plan()
            self._execute()
            self._knowledge()
            sleep(INTERVAL)

def main():
    engine = Engine()
    threading.Thread(target=engine.listen, daemon=True).start()
    engine.start()

if __name__ == "__main__":
    main()