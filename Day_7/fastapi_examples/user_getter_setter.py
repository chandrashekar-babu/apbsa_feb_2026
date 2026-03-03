def property(fn):
    def internal_decorator(cls, instance):
        def getter(self, attr):
            if attr == fn.__qualname__:
                return fn(self)

        setattr(instance, "__getattr__", getter)

class User:

    #@property
    #def name(self):
    #    return "John"

    def __getattr__(self, attr):
        if attr == "name":
            return "John"

u = User()
u.name


