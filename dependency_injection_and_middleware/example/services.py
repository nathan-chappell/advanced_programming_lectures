import logging
import json
from random import random
from asyncio import sleep

from service_provider import service_provider

log = logging.getLogger(__name__)

# artificial delays for simulation

def small_delay():
    return sleep(random())

def medium_delay():
    return sleep(1 + .5 * random())

def big_delay():
    return sleep(2 + random())

@service_provider.register
class HelloService:
    """Service which says hello"""
    async def get_response(self, content):
        await medium_delay()
        if 'hello' in content.lower():
            return 'Hello to you.'
        if 'goodbye' in content.lower():
            return 'Goodbye.'
        return 'Say hi or something!'

class DataAdapterException(Exception):
    def __init__(self):
        super().__init__(self.__class__.__name__)

class AlreadyExists(DataAdapterException): pass
class NotFound(DataAdapterException): pass

@service_provider.singleton
class DataStore(dict):
    """Backend data store"""
    def __init__(self):
        log.info(f'Creating [singleton] DataStore')
        super().__init__()

@service_provider.session
class DataAdapter:
    """CRUD-Adapter to access backend store"""
    def __init__(self, store: 'DataStore'):
        log.info(f'Creating [session] DataAdapter')
        self.store = store

    def check_exists(self, key):
        if key not in self.store:
            raise NotFound()

    def check_not_exists(self, key):
        if key in self.store:
            raise AlreadyExists()

    async def create(self, key, value):
        await medium_delay()
        self.check_not_exists(key)
        self.store[key] = value

    async def read(self, key):
        await small_delay()
        self.check_exists(key)
        return self.store[key]

    async def update(self, key, value):
        await big_delay()
        self.check_exists(key)
        self.store[key] = value

    async def delete(self, key):
        await medium_delay()
        self.check_exists(key)
        del self.store[key]

    async def query(self, key):
        await big_delay()
        return { k:v for k,v in self.store.items() if key.lower() in k.lower() }

@service_provider.register
class SearchService:
    """Business Search logic"""
    def __init__(self, adapter: 'DataAdapter'):
        log.info(f'Creating [scope] SearchService')
        self.adapter = adapter
    
    async def get(self, key):
        return self.adapter.read(key)

    async def create(self, key, value):
        await self.adapter.create(key, value)

    async def search(self, key):
        response = await self.adapter.query(key)
        return json.dumps(response)


@service_provider.register
class FooService:
    """Some service that also requires a DataAdapter"""
    def __init__(self, adapter: 'DataAdapter'):
        log.info(f'Creating [scope] FooService')
        self.adapter = adapter
