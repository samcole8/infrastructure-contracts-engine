from ice.engine import Probe, Connection, LocalConnection

class FakeCapability:
    def __init__(self):
        self.state = None

def test_probe_sets_state_true_on_success():
    capability = FakeCapability()
    probe = Probe(capability, "echo hi")
    probe.run(lambda script: True)
    assert capability.state is True

def test_probe_sets_state_false_on_failure():
    capability = FakeCapability()
    probe = Probe(capability, "exit 1")
    probe.run(lambda script: False)
    assert capability.state is False

def test_local_connection_runs_probe():
    capability = FakeCapability()
    conn = LocalConnection()
    conn.probes.append(Probe(capability, "exit 0"))
    conn.run()
    assert capability.state is True
