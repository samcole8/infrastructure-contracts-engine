from ice.model import Requirement as ModelRequirement
from ice.engine.model.capability import Capability

class Requirement(ModelRequirement):

    @property
    def has_static_capabilities(self):
        for c in self.capabilities:
            if c.__class__ == Capability:
                return True
        return False