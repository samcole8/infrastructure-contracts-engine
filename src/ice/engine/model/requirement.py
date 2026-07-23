from ice.model import Requirement as ModelRequirement
from ice.engine.model.capability import Capability

class Requirement(ModelRequirement):

    def __init__(self, name, src, capabilities, contract):
        super().__init__(name, src, None, capabilities, contract)

    @property
    def has_static_capabilities(self):
        for c in self.capabilities:
            if c.__class__ == Capability:
                return True
        return False