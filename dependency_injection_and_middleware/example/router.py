from functools import wraps

from util import Message, Response
from service_provider import service_provider
import services

class Router:
    def __init__(self):
        self.routes = {}

    # decorator factory
    def route(self, path: str):
        def decorator(f: 'Callable'):
            self.routes[path] = f
            return f
        return decorator
    
    def not_found_handler(self, message: Message):
        return Response(f'<Router>: path {message.path} not found')

    def handle_message(self, message: Message) -> Response:
        handler = self.routes.get(message.path, self.not_found_handler)
        with service_provider.in_session() as session_provider:
            args = session_provider.get_args(handler)
        args['message'] = message
        return handler(**args)

# global router
router = Router()
