from ice.engine.builder import build, build_contract, tokenise

def make_config():
    return {
        "systems": [
            {"name": "proxmox", "target": "10.0.0.1", "username": "root", "password": "pw"},
            {"name": "heartbeat_vm", "target": "10.0.0.2", "username": "root", "password": "pw"},
        ],
        "capabilities": [
            {"name": "outbound_allowed", "src": "proxmox", "dst": "heartbeat_vm",
             "script": "check_outbound.sh", "origin": "dst"},
            {"name": "heartbeat_active", "src": "proxmox", "dst": "heartbeat_vm", "state": True},
        ],
        "requirements": [
            {"name": "proxmox_heartbeat", "src": "heartbeat_vm",
             "contract": "outbound_allowed or heartbeat_active"},
        ],
    }

def test_build_wires_declared_and_live_capabilities_correctly():
    systems, connections = build(make_config())
    proxmox = next(s for s in systems if s.name == "proxmox")
    declared = next(c for c in proxmox.capabilities if c.name == "heartbeat_active")
    live = next(c for c in proxmox.capabilities if c.name == "outbound_allowed")
    assert declared.state is True
    assert live.state is None

def test_probe_placed_on_correct_connection_via_origin():
    systems, connections = build(make_config())
    heartbeat_conn = next(c for c in connections if getattr(c, "system", None) and c.system.name == "heartbeat_vm")
    assert "outbound_allowed" in [p.capability.name for p in heartbeat_conn.probes]

def test_requirement_evaluates_correctly_end_to_end():
    systems, connections = build(make_config())
    heartbeat_vm = next(s for s in systems if s.name == "heartbeat_vm")
    assert heartbeat_vm.requirements[0].evaluate() is True

def test_build_contract_resolves_names_and_raises_on_unknown():
    import pytest
    caps = {"a": "A"}
    assert build_contract("a", caps) == "A"
    with pytest.raises(KeyError):
        build_contract("b", caps)
