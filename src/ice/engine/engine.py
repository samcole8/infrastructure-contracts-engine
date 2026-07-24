import threading
import time

from ice.engine.mape import tick

class Engine:
    
    def __init__(self, interval):
        self.interval = interval
        self.systems = []
        self.running = False

    def loop(self):
        while self.running:
            print(f"WAITING {self.interval}")
            time.sleep(self.interval)
            tick(self.systems)

    def reload(self, systems):
        print("ENGINE RELOAD")
        self.stop()
        self.systems = systems
        passes, fails, errors = tick(systems)
        # self.start() # de-comment when engine is threaded
        return passes, fails, errors

    def start(self):
        self.running = True
        print("ENGINE START")
        self.loop()

    def stop(self):
        print("ENGINE STOP")

