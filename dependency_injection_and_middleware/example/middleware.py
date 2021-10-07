import logging
from functools import reduce

from util import Message, Response
import routes
from authorization import authorization as global_authorizer

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
# MessageHandler: Message -> Response

def middleware_reducer(acc: 'MessageHandler', _next: 'Middleware') -> 'MessageHandler':
    return _next(acc)

def null_handler(message: 'Message') -> 'Response':
    return Response()

def build_middleware(middlewares: 'List[Middleware]') -> 'MessageHandler':
    return reduce(middleware_reducer, reversed(middlewares), null_handler)
    
## Middlewares...

def logger(_next: 'MessageHandler') -> 'MessageHandler':
    def handler(message: 'Message') -> 'Response':
        logging.info(f'<Logger, incoming>: {message}')
        response = _next(message)
        logging.info(f'<Logger, outgoing>: {response}')
        return response
    return handler

def error_handler(_next):
    def handler(message):
        try:
            return _next(message)
        except Exception as e:
            return Response(f'<ErrorHandler>: {e}')
    return handler

# MUST BE LAST!  Unconditionally short-circuits pipeline
def router(_next):
    def handler(message):
        response = routes.router.handle_message(message)
        return response
    return handler

def authorization(_next):
    def handler(message):
        global_authorizer.authorize_message(message)
        return _next(message)
    return handler
