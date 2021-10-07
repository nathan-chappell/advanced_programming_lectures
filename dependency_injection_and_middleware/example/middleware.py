import logging
from functools import reduce

from util import Message, Response

logging.basicConfig()
# MessageHandler: Message -> Response

def logger(_next: 'MessageHandler') -> 'MessageHandler':
    def handler(message: 'Message') -> 'Response':
        logging.info(f'<Logger, incoming>: {message}')
        response = _next(message)
        logging.info(f'<Logger, outgoing>: {response}')
        return response
    return handler

def middleware_reducer(acc: 'MessageHandler', _next: 'Middleware') -> 'MessageHandler':
    return _next(acc)

def null_handler(message: 'Message') -> 'Response':
    return Response()

def build_middleware(middlewares: 'List[Middleware]') -> 'MessageHandler':
    # TODO: implement
    # want...
    #   message -> error_handler(authorization(router(null_handler)))(message)
    ...
    
