from util import Message, Response
from router import router
from authorization import authorization

@router.route('/index')
def index(message: Message, hello_service: 'HelloService') -> Response:
    response = hello_service.get_response(message.content)
    return Response(response)

@router.route('/new')
@authorization.required
def new(message: Message, search_service: 'SearchService') -> Response:
    k,v = message.content.split(',')
    return search_service.create(k,v)


@router.route('/get')
def get(message: Message, search_service: 'SearchService') -> Response:
    key = message.content
    return search_service.get(key)


@router.route('/search')
def search(
        message: Message,
        search_service: 'SearchService',
        foo_service: 'FooService',
    ) -> Response:
    key = message.content
    return search_service.search(key)
