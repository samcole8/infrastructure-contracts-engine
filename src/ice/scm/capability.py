class Capability:
    def __init__(self, name, src, dst):
        self.name = name
        self.src = src
        self.dst = dst
        self.requirements = []
        self.state = None

    def evaluate(self):
        return self.state
