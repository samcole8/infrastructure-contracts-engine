"""Simple manual integration tests."""

from ice.engine import Probe, Connection, build
from ice.scm import System, Capability

def test_probe(ip):
    system = System("test_target")  # or import from ice.scm if needed
    connection = Connection(
        system=system,
        target=ip,
        username="root",
        password="password",
    )

    capability = Capability("outbound_allowed", system, system)
    connection.probes.append(Probe(capability, "exit 0"))

    connection.run()

    print(f"capability.state = {capability.state}")
    assert capability.state is True, "expected script to succeed"
    print("Test 1 OK — SSH connection and script execution confirmed working.")

def test_full_pipeline(ip):
    config = {
        "systems": [
            {"name": "s1", "target": ip, "username": "root", "password": "password"},
            {"name": "s2"},
        ],
        "capabilities": [
            {"name": "c1", "src": "s1", "dst": "s2", "script": "exit 0"},
            {"name": "c2", "src": "s1", "dst": "s2", "state": False},
            {"name": "c3", "src": "s1", "dst": "s2", "state": True},
        ],
        "requirements": [
            {"name": "r1", "src": "s2",
             "contract": "((c1 or c2) and c3)"},
            {"name": "r2", "src": "s2",
             "contract": "c2"},
        ],
    }

    systems, connections = build(config)

    results = {}
    for system in systems:
        for requirement in system.requirements:
            results[requirement.name] = requirement.evaluate()

    if results["r1"] is None and results["r2"] is False:
        print("Test 2 OK - Contract None propogation evaluated in full build")
    
    for connection in connections:
        connection.run()

    results = {}
    for system in systems:
        for requirement in system.requirements:
            results[requirement.name] = requirement.evaluate()

    if results["r1"] is True and results["r2"] is False:
        print("Test 3 OK - Full build evaluated")
        print("((c1 or c2) and c3)")

if __name__ == "__main__":
    ip=input("Enter target IP: ")
    test_probe(ip)
    test_full_pipeline(ip)
