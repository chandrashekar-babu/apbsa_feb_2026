from threading import Lock
class Event:

    def __init__(self):
        self.status = False
        self.lock = Lock()

    def set(self):
        self.status = True
        
    def is_set(self):
        return self.status

    def clear(self):
        with self.lock:
            self.status = False

    def wait(self):
        pass # Actual implemention: block if status is False, until 
             # the status becomes True (by some other thread)
             
            