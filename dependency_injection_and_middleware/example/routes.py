from util import Message, Response
from router import router
from authorization import authorization

@router.route('/index')
async def index(message: Message, hello_service: 'HelloService') -> Response:
    result = await hello_service.get_response(message.content)
    return Response(result)

@router.route('/new')
@authorization.required
async def new(message: Message, search_service: 'SearchService') -> Response:
    k,v = message.content.split(',')
    await search_service.create(k,v)
    return Response("created.")


@router.route('/get')
async def get(message: Message, search_service: 'SearchService') -> Response:
    key = message.content
    result = await search_service.get(key)
    return Response(result)


@router.route('/search')
async def search(
        message: Message,
        search_service: 'SearchService',
        foo_service: 'FooService',
    ) -> Response:
    key = message.content
    result = await search_service.search(key)
    return Response(result)
