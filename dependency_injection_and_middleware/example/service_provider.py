from inspect import signature
from contextlib import contextmanager

class ServiceProvider:
    singleton_cache = {}
    services = {}
    session_services = set()

    def _construct(self, name):
        cls = self.services[name]
        args = self.get_args(cls.__init__)
        return cls(**args)

    def get_cached(self, cache, name):
        instance = cache.get(name, None)
        if instance is None:
            instance = self._construct(name)
            cache[name] = instance
        return instance

    def construct(self, service: 'str or Type'):
        name = service if type(service) == str else service.__name__
        if name in self.singleton_cache:
            return self.get_cached(self.singleton_cache, name)
        if name in self.session_services and getattr(self, 'session', False):
            return self.get_cached(self.session, name)
        return self._construct(name)
    
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
        self.register(cls)

    def session(self, cls):
        self.session_services.add(cls.__name__)
        self.register(cls)

    @contextmanager
    def in_session(self):
        provider_with_session = ServiceProvider()
        provider_with_session.session = {}
        yield provider_with_session

service_provider = ServiceProvider()
