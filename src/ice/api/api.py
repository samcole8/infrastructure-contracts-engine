from time import sleep

TEMP_CONFIG = {
    "systems": [
        {"name": "s1", "target": input("Enter IP address: "), "username": "root", "password": "password"},
        {"name": "s2"},
        {"name": "s3"},
    ],
    "capabilities": [
        {"name": "c1", "src": "s1", "origin": "src", "script": "exit 0"},
        {"name": "c2", "src": "s1", "state": True},
        {"name": "c3", "src": "s1", "state": True},
    ],
    "requirements": [
        {"name": "r1", "src": "s2",
            "contract": "((c1 or c2) and c3)"},
        {"name": "r2", "src": "s2",
            "contract": "c2"},
    ],
}

class API:
    
    def listen(self):
        sleep(1.0)
        return TEMP_CONFIG

    def respond(self, msg):
        sleep(0.2)
        if msg:
            print("API REPORTING FAILURE")
        else:
            print("API REPORTING SUCCESS")