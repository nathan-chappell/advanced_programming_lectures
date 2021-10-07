from middleware import build_middleware, router, authorization, error_handler, logger
from util import Message, Response

class Server:
    """basic server.  Used with net_server."""
    def __init__(self, middlewares: 'List[Middleware]'):
        self.pipeline = build_middleware(middlewares)

    async def handle_message(self, message: Message) -> Response:
        return await self.pipeline(message)

server = Server([logger, error_handler, authorization, router])
