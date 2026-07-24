from time import sleep

TEMP_CONFIG = {
    "systems": [
        {"name": "s1", "target": input("Enter IP address: "), "username": "root", "password": "password"},
        {"name": "s2"},
        {"name": "s3"},
    ],
    "capabilities": [
        {"name": "c1", "system": "s1", "origin": "s1", "cmd": "exit 0"},
        {"name": "c2", "system": "s1", "state": False},
        {"name": "c3", "system": "s1", "state": True},
    ],
    "requirements": [
        {"name": "r1", "system": "s2",
            "contract": "((c1 or c2) and c3)"},
        {"name": "r2", "system": "s2",
            "contract": "c2"},
    ],
}

class API:
    
    def listen(self):
        sleep(1.0)
        return TEMP_CONFIG

    def respond(self, passes, fails, errors):
        sleep(0.2)
        alerts = fails + errors
        if len(alerts) > 0:
            print(f"API WARNING:\n{alerts}")
        else:
            print("API OK")