import logging
from functools import reduce

from util import Message, Response
import routes
from authorization import authorization as global_authorizer

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
# MessageHandler: (async) Message -> Response

def middleware_reducer(acc: 'MessageHandler', _next: 'Middleware') -> 'MessageHandler':
    return _next(acc)

async def null_handler(message: 'Message') -> 'Response':
    return Response()

def build_middleware(middlewares: 'List[Middleware]') -> 'MessageHandler':
    return reduce(middleware_reducer, reversed(middlewares), null_handler)
    
## Middlewares...

count = 0

_logger = logging.getLogger('logger')

def logger(_next: 'MessageHandler') -> 'MessageHandler':
    async def handler(message: 'Message') -> 'Response':
        global count
        _count = count
        count += 1
        _logger.info(f'[{_count:4} <-- ]: {message}')
        response = await _next(message)
        _logger.info(f'[{_count:4} --> ]: {response}')
        return response
    return handler

def error_handler(_next):
    async def handler(message):
        try:
            return await _next(message)
        except Exception as e:
            return Response(f'<ErrorHandler>: {e}')
    return handler

# MUST BE LAST!  Unconditionally short-circuits pipeline
def router(_next):
    async def handler(message):
        response = await routes.router.handle_message(message)
        return response
    return handler

def authorization(_next):
    async def handler(message):
        global_authorizer.authorize_message(message)
        return await _next(message)
    return handler
