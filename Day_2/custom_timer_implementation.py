from threading import Thread, Event

class Timer(Thread):
    def __init__(self, interval, func, args=(), kwargs={}, *targs, **tkwargs):
        super().__init__(*targs, **tkwargs)
        self.interval = interval
        self.func = func
        self.fn_args = args
        self.fn_kwargs = kwargs
        self.cancelled = Event()
        self.daemon = True

    def run(self):
        if not self.cancelled.wait(self.interval):
            self.func(*self.fn_args, **self.fn_kwargs)

    def cancel(self):
        self.cancelled.set()