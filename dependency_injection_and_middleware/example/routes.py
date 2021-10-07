from util import Message, Response
from router import router

@router.route('/index')
def index(message: Message, hello_service: 'HelloService') -> Response:
    response = hello_service.get_response(message.content)
    return Response(response)


@router.route('/query')
def index(message: Message) -> Response:
    return Response('hello to you')
