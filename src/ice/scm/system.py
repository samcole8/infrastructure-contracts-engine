class System:
    def __init__(self, name):
        self.name = name
        self.capabilities = []
        self.requirements = []

class Requirement:
    def __init__(self, name, src, contract):
        self.name = name
        self.src = src
        self.contract = contract

    def evaluate(self):
        return self.contract.evaluate()

class Capability:
    def __init__(self, name, src, dst):
        self.name = name
        self.src = src
        self.dst = dst
        self.state = None

    def evaluate(self):
        return self.state
