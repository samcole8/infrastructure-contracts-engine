from contextlib import contextmanager
from fabric import Connection
import subprocess

from ice.model import System as ModelSystem
from ice.engine.model.capability import DynamicCapability

class System(ModelSystem):

    def __init__(self, name):
        super().__init__(name)
        self.probes = []

    @contextmanager
    def connect(self):
        yield lambda c: c.state

    def poll(self):
        modified = set()
        with self.connect() as connection:
            i = 0
            while i < len(self.probes):
                p = self.probes[i]
                modified.update(p.probe(connection))
                if p.__class__ is not DynamicCapability:
                    del self.probes[i]
                else:
                    i += 1
        return modified

class RemoteSystem(System):
    def __init__(self, name, target, username, password):
        super().__init__(name)
        self.target = target
        self.username = username
        self.password = password

    @contextmanager
    def connect(self):
        try:
            connection = Connection(host=self.target, user=self.username, connect_kwargs={"password": self.password})
            yield lambda c: connection.run(c.cmd, hide=True, warn=True).return_code == 0
        finally:
            connection.close()

class LocalSystem(System):

    @contextmanager
    def connect(self):
        yield lambda c: subprocess.run(["bash", "-c", c.cmd], capture_output=True).returncode == 0
