from dataclasses import dataclass
# TODO: implement middleware
from middleware import router, authorization, error_handler, logger

@dataclass
class Message:
    subject: str
    path: str
    content: str


@dataclass
class Response:
    content: str


class Server:
    def __init__(self, middlewares: 'List[Middleware]'):
        self.pipeline = build_middleware(middlewares)

    def handle_message(self, message: Message) -> Response:
        return self.pipeline(message)

if __name__ == '__main__':
    messages = [
        Message('hello','/index',''),
        Message('query','/search','foo'),
        Message('delete','/foo','[code=wrong_code]'),
        Message('query','/search','foo'),
        Message('delete','/foo','[code=secret_code]'),
        Message('query','/search','foo'),
        Message('asdf','/qwer','zxcv'),
    ]

    # TODO: fix order of middleware
    server = Server([router, authorization, error_handler])

    for message in messages:
        print(message)
        response = server.handle_message(message)
        print(response)
