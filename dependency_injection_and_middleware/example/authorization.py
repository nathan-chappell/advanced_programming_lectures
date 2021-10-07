import re
from functools import wraps

# from service_provider import service_provider
from util import Response

# @service_provider.session
class Authorization:
    password_re = re.compile(r'(\[code=(?P<password>\w*)\])?(?P<content>.*)')

    def authorize(self, password):
        if password == 'secret_code':
            return 'authorized'
        return 'not-authorized'

    def authorize_message(self, message: 'Message'):
        match = self.password_re.match(message.content)
        password = match.group('password')
        content = match.group('content')
        message.content = content
        message.context['authorization'] = self.authorize(password)

    def required(self, handler):
        @wraps(handler)
        async def wrapped(message: 'Message', *args, **kwargs):
            if message.context.get('authorization',None) == 'authorized':
                response = await handler(message, *args, **kwargs)
            else:
                response = Response('Not Authorized')
            return response
        return wrapped

authorization = Authorization()
