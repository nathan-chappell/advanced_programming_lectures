import logging
import json

from service_provider import service_provider

@service_provider.register
class HelloService:
    def get_response(self, content):
        if 'hello' in content.lower():
            return 'Hello to you.'
        if 'goodbye' in content.lower():
            return 'Goodbye.'
        return 'Say hi or something!'

class DataAdapterException(Exception): pass
class AlreadyExists(DataAdapterException): pass
class NotFound(DataAdapterException): pass

@service_provider.singleton
class DataAdapter:
    def __init__(self):
        logging.info(f'Creating DataAdapter')
        self.store = {}

    def check_exists(self, key):
        if key not in self.store:
            raise NotFound()

    def check_not_exists(self, key):
        if key in self.store:
            raise AlreadyExists()

    def create(self, key, value):
        self.check_not_exists(key)
        self.store[key] = value

    def read(self, key):
        self.check_exists(key)
        return self.store[key]

    def update(self, key, value):
        self.check_exists(key)
        self.store[key] = value

    def delete(self, key):
        self.check_exists(key)
        del self.store[key]

    def query(self, key):
        return { k:v for k,v in self.store.items() if key.lower() in k.lower() }

@service_provider.register
class SearchService:
    def __init__(self, adapter: 'DataAdapter'):
        self.adapter = adapter
    
    def get(self, key):
        return self.adapter.read(key)

    def create(self, key, value):
        self.adapter.create(key, value)

    def search(self, key):
        return json.dumps(self.adapter.query(key))
