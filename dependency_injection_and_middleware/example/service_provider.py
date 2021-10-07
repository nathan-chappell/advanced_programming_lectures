from inspect import signature

class ServiceProvider:
    singleton_cache = {}

    def __init__(self):
        self.services = {}

    def construct(self, service: 'str or Type'):
        name = service if type(service) == str else service.__name__
        is_singleton = name in self.singleton_cache
        if is_singleton:
            singleton = self.singleton_cache.get(name, None)
            if singleton is not None:
                return singleton
        cls = self.services[name]
        args = self.get_args(cls.__init__)
        instance = cls(**args)
        if is_singleton:
            self.singleton_cache[name] = instance
        # TODO: respect signature kw/positional params...
        return instance
    
    def has_service(self, service):
        if type(service) != str:
            service = service.__name__
        return service in self.services

    def get_args(self, fn):
        sig = signature(fn)
        args = {}
        sig = signature(fn)
        for name,parameter in sig.parameters.items():
            annotation = parameter.annotation
            if self.has_service(annotation):
                args[name] = self.construct(annotation)
        return args


    def register(self, cls):
        self.services[cls.__name__] = cls

    def singleton(self, cls):
        self.singleton_cache[cls.__name__] = None
        self.services[cls.__name__] = cls

service_provider = ServiceProvider()
