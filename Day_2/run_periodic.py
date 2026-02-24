from threading import Thread

class RunPeriodic(Thread):
    def __init__(self, interval, fn, *fn_args, **fn_kwargs):
        super().__init__()
        self.interval = interval
        self.fn = fn
        self.fn_args = fn_args
        self.fn_kwargs = fn_kwargs
        self.cancel = False

    def run(self):
        from time import sleep
        while not self.cancel:
            sleep(self.interval)
            self.fn(*self.fn_args, **self.fn_kwargs)

    def stop(self):
        self.cancel = True
                    
