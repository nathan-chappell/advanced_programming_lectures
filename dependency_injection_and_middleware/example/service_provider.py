from inspect import signature

class ServiceProvider
    def __init__(self)
        self.services = {}

    def construct(self, service: 'str or Type'):
        name = service if type(service) == str else service.__name__
        cls = self.services[name]
        args = self.get_args(cls.__init__)
        # TODO: respect signature kw/positional params...
        return cls(**args)
    
    def has_service(self, service):
        if type(service) != str:
            service = service.__name__
        return service in self.services

    def get_args(self, fn):
        sig = signature(fn)
        args = {}
        sig = signature(fn)
        for name,parameter in sig.items():
            annotation = parameter.annotation
            if self.has_service(annotation):
                args[name] = self.construct(annotation)
        return args


    def register(self, cls):
        self.services[cls.__name__] = cls

service_provider = ServiceProvider()
