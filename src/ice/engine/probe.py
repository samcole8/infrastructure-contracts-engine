import subprocess
from contextlib import contextmanager
from fabric import Connection as FabricConnection

def open_ssh(target, username, password):
    return FabricConnection(host=target, user=username, connect_kwargs={"password": password})

class Probe:
    
    def __init__(self, capability, script):
        self.capability = capability
        self.script = script
    
    def run(self, runner):
        self.capability.state = runner(self.script)

class Connection:
    def __init__(self, system, target, username, password):
        self.system = system
        self.target = target
        self.username = username
        self.password = password
        self.probes = []

    @contextmanager
    def connect(self):
        client = open_ssh(self.target, self.username, self.password)
        try:
            def runner(script):
                result = client.run(script, hide=True, warn=True)
                return result.return_code == 0
            yield runner
        finally:
            client.close()
    
    def run(self):
        if self.probes:
            with self.connect() as session:
                for probe in self.probes:
                    probe.run(session)

class LocalConnection(Connection):
    
    def __init__(self):
        super().__init__(None, None, None, None)
        self.probes = []

    @contextmanager
    def connect(self):
        def runner(script):
            result = subprocess.run(["bash", "-c", script], capture_output=True)
            return result.returncode == 0
        yield runner
