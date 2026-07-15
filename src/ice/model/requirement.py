class Requirement:
    def __init__(self, name, src, dst, capabilities, contract):
        self.name = name
        self.src = src
        self.dst = dst
        self.capabilities = []
        self.contract = contract

    def evaluate(self):
        return self.contract.evaluate()
