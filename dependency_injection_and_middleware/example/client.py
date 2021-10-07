import asyncio
from random import randint

from util import Message

# pool of message examples for random selection
messages = [
    Message('/index','hello there'),
    Message('/index','goodbye sir'),
    Message('/search','foo'),
    Message('/new','foo,this is an example'),
    Message('/new','[code=secret_code]foo,this is an example'),
    Message('/new','[code=wrong_code]foo,this is an example'),
    Message('/search','foo'),
    Message('/qwer','zxcv'),
]

def random_message():
    """select a message at random"""
    return messages[randint(0, len(messages)-1)]

def encode_message(message):
    """prepare message to send over the wire"""
    s = f'{message.path}\n{message.content}'
    return bytes(s,'ascii')

async def send_random_message():
    """gets a connection and sends a message at random"""
    r,w = await asyncio.open_connection('localhost', 8080)
    message = random_message()
    encoded = encode_message(message)
    w.write(encoded)
    w.write_eof()
    response = await r.read()
    print(response)
    w.close()
    return response

async def send_messages(n=4, batch_size=4):
    """sends n batches of (batch_size) messages"""
    for batch in range(n):
        await asyncio.gather(*[send_random_message() for i in range(batch_size)])

asyncio.run(send_messages())
