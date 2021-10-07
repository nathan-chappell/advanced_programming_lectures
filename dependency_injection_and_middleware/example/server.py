from middleware import build_middleware, router, authorization, error_handler, logger
from util import Message, Response

class Server:
    def __init__(self, middlewares: 'List[Middleware]'):
        self.pipeline = build_middleware(middlewares)

    def handle_message(self, message: Message) -> Response:
        return self.pipeline(message)

if __name__ == '__main__':
    messages = [
        Message('/index','hello there'),
        Message('/index','goodbye sir'),
        Message('/search','foo'),
        Message('/new','foo,this is an example'),
        Message('/search','foo'),
        Message('/foo','[code=wrong_code]'),
        Message('/foo','[code=secret_code]'),
        Message('/search','foo'),
        Message('/qwer','zxcv'),
    ]

    # TODO: fix order of middleware
    server = Server([logger, error_handler, authorization, router])

    for message in messages:
        # print(message)
        response = server.handle_message(message)
        # print(response)
