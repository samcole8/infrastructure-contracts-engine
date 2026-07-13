from time import sleep

class Engine:

    def __init__(self, interval):
        self.interval = interval
        self.systems = []
        self.probes = []
    
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

    def reload(self, systems, probes):
        # Update knowledge base
        self.systems = systems
        self.probes = probes
        return True
