from threading import Lock
class Event:

    def __init__(self):
        self.status = False
        self.lock = Lock()

    def set(self):
        with self.lock:
            self.status = True
        
    def is_set(self):
        with self.lock:
            return self.status

    def clear(self):
        with self.lock:
            self.status = False
            