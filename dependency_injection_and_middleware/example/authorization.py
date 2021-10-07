import re
from functools import wraps

from util import Response

class Authorization:
    """Encapsulates "Authorization" for messages"""

    # parse the password from the message
    password_re = re.compile(r'(\[code=(?P<password>\w*)\])?(?P<content>.*)')

    def authorize(self, password):
        """Checks to see what the given password is authorized for"""
        if password == 'secret_code':
            return 'authorized'
        return 'not-authorized'

    def authorize_message(self, message: 'Message'):
        """Attaches authorization information to the Message.context"""
        match = self.password_re.match(message.content)
        password = match.group('password')
        content = match.group('content')
        message.content = content
        message.context['authorization'] = self.authorize(password)

    def required(self, handler):
        """Decorator for MessageHandlers that require Authorization"""
        @wraps(handler)
        async def wrapped(message: 'Message', *args, **kwargs):
            if message.context.get('authorization',None) == 'authorized':
                response = await handler(message, *args, **kwargs)
            else:
                response = Response('Not Authorized')
            return response
        return wrapped

authorization = Authorization()
