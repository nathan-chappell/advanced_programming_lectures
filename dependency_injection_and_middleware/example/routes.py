from util import Message, Response
from router import router

@router.route('/index')
def index(message: Message, hello_service: 'HelloService') -> Response:
    response = hello_service.get_response(message.content)
    return Response(response)


@router.route('/search')
def index(message: Message, search_service: 'SearchService') -> Response:
    return Response('hello to you')
