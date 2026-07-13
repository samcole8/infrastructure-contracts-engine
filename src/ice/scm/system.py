class System:
    def __init__(self, name):
        self.name = name
        self.capabilities = []
        self.contracts = []

class Capability:
    def __init__(self, name, system):
        self.name = name
        self.state = None
        self.system = system

    def evaluate(self):
        return self.state
