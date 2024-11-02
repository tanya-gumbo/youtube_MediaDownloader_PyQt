from PyQt6.QtQml import kwargs


class Container:
    def __init__(self):
        self.registry = {}

    def register(self, name, cls, *args, **kwargs):
        self.registry[name] = (cls, args, kwargs)

    def resolve(self, name):
        cls, args, kwargs = self.registry[name]
        return cls(args, kwargs)