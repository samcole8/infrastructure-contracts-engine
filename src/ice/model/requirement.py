class Requirement:
    def __init__(self, name, src, capabilities, contract):
        self.name = name
        self.src = src
        self.capabilities = []
        self.contract = contract

    def evaluate(self):
        return self.contract.evaluate()
