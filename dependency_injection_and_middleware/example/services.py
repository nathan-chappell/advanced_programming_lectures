

from service_provider import service_provider

@service_provider.register
class HelloService:
    def get_response(self, content):
        if 'hello' in content.lower():
            return 'Hello to you.'
        if 'goodbye' in content.lower():
            return 'Goodbye.'
        return 'Say hi or something!'
