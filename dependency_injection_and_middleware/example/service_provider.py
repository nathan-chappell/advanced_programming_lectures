from inspect import signature
from contextlib import contextmanager

class ServiceProvider:
    """ServiceProvider is the DI handling class"""
    # what we can construct
    services: 'Dict[Name, ServiceClass]' = {}
    # singletons are tracked statically
    singleton_cache = {}
    # which services have 'session scope'
    session_services = set()

    def _construct(self, name):
        """Unconditionally creates new {name}-Service.  Recurse into get_args"""
        cls = self.services[name]
        args = self.get_args(cls.__init__)
        return cls(**args)

    def get_cached(self, cache, name):
        """Checks cache for service, creates if misses"""
        instance = cache.get(name, None)
        if instance is None:
            instance = self._construct(name)
            cache[name] = instance
        return instance

    def construct(self, service: 'str or Type'):
        """Dispatches based on service lifetime"""
        name = service if type(service) == str else service.__name__
        if name in self.singleton_cache:
            return self.get_cached(self.singleton_cache, name)
        if name in self.session_services and getattr(self, 'session', None) is not None:
            return self.get_cached(self.session, name)
        return self._construct(name)
    
    def has_service(self, service):
        if type(service) != str:
            service = service.__name__
        return service in self.services

    def get_args(self, fn):
        """Uses introspection to get the args for a fn (creates with construct)"""
        sig = signature(fn)
        args = {}
        sig = signature(fn)
        for name,parameter in sig.parameters.items():
            annotation = parameter.annotation
            if self.has_service(annotation):
                args[name] = self.construct(annotation)
        return args

    def register(self, cls):
        """Decorator to register at lifetime [Scope]"""
        self.services[cls.__name__] = cls

    def singleton(self, cls):
        """Decorator to register at lifetime [Singleton]"""
        self.singleton_cache[cls.__name__] = None
        self.register(cls)

    def session(self, cls):
        """Decorator to register at lifetime [Session]"""
        self.session_services.add(cls.__name__)
        self.register(cls)

    @contextmanager
    def in_session(self):
        """Returns provider which is tracking [Session] services"""
        provider_with_session = ServiceProvider()
        provider_with_session.session = {}
        yield provider_with_session

service_provider = ServiceProvider()
