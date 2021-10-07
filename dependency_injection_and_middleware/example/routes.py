from util import Message, Response
from router import router

@router.route('/index')
def index(message: Message) -> Response:
    return Response('hello to you')
