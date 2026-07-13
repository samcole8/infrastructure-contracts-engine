from time import sleep

class Engine:

    def __init__(self, interval):
        self._knowledge_cache = None
        self.requirements = []
        self.interval = interval
    
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
        pass

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
            sleep(self.interval)