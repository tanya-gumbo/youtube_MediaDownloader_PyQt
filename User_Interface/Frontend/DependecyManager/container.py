class Container:
    def __init__(self):
        self.registry = {}

    def register(self, name, cls, *args, **kwargs):
        self.registry[name] = (cls, args, kwargs)

    def resolve(self, name):
        if name in self.registry:
            cls, args, kwargs = self.registry[name]
            return cls(*args, **kwargs)
        else:
            return None