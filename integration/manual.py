"""Simple manual integration tests."""

from ice.engine import build
from ice.engine.mape import tick

def test_full_pipeline(ip):
    config = {
        "systems": [
            {"name": "s1", "target": ip, "username": "root", "password": "password"},
            {"name": "s2"},
            {"name": "s3"},
        ],
        "capabilities": [
            {"name": "c1", "src": "s1", "dst": "s2", "origin": "src", "script": "exit 0"},
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

    systems = build(config)
    tick(systems)

if __name__ == "__main__":
    ip=input("Enter target IP: ")
    test_full_pipeline(ip)
