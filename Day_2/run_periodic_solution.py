from threading import Thread, Event
from time import sleep

class RunPeriodic(Thread):
    def __init__(self, interval, func, args=(), kwargs={}, *targs, **tkwargs):
        super().__init__(*targs, **tkwargs)
        self.interval = interval
        self.func = func
        self.fn_args = args
        self.fn_kwargs = kwargs
        self._stop_event = Event()
        self.daemon = True

    def run(self):
        while not self._stop_event.wait(self.interval):
            self.func(*self.fn_args, **self.fn_kwargs)

    def stop(self):
        self._stop_event.set()