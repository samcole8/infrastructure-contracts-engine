class System:

    def __init__(self, name, username=None, password=None):
        self.name = name
        self.username = username
        self.password = password

class LocalSystem(System):
    def connect(self):
        pass
