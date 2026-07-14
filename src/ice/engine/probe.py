class Probe:
    
    def __init__(self, capability, script):
        self.capability = capability
        self.script = script
    
    def run(self, session):
        pass

class Connection:
    def __init__(self, system, target, username, password):
        self.system = system
        self.target = target
        self.username = username
        self.password = password
        self.probes = []

    def run(self):
        with self.connect() as session:
            for probe in self.probes:
                probe.run(session)
    
    def connect(self):
        pass

class LocalConnection(Connection):
    
    def __init__(self):
        super().__init__(system=None, target=None, username=None, password=None)

    def connect(self):
        pass