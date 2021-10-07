from middleware import build_middleware, router, authorization, error_handler, logger
from util import Message, Response

class Server:
    def __init__(self, middlewares: 'List[Middleware]'):
        self.pipeline = build_middleware(middlewares)

    def handle_message(self, message: Message) -> Response:
        return self.pipeline(message)

if __name__ == '__main__':
    messages = [
        Message('hello','/index','hello there'),
        Message('goodbye','/index','goodbye sir'),
        Message('query','/search','foo'),
        Message('delete','/foo','[code=wrong_code]'),
        Message('query','/search','foo'),
        Message('delete','/foo','[code=secret_code]'),
        Message('query','/search','foo'),
        Message('asdf','/qwer','zxcv'),
    ]

    # TODO: fix order of middleware
    server = Server([logger, error_handler, authorization, router])

    for message in messages:
        print(message)
        response = server.handle_message(message)
        print(response)
