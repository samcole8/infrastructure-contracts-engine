from ice.model import Capability as ModelCapability

class Capability(ModelCapability):
    def __init__(self, name, src, origin):
        super().__init__(name, src, None)
        self.origin = origin

    def probe(self, connection):
        return self.requirements

class DynamicCapability(Capability):
    def __init__(self, name, src, origin, cmd):
        super().__init__(name, src, origin)
        self.cmd = cmd

    def probe(self, connection):
        old = self.state
        self.state = connection(self)
        return self.requirements if self.state != old else set()
