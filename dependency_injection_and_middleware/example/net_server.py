import asyncio
import logging

from server import server
from util import Message

logging.getLogger('services').setLevel(logging.WARN)

def parse_message(message):
    path, content = message.split("\n")
    return Message(path, content)

def encode_response(response):
    return bytes(str(response), 'ascii')

async def handler(reader, writer):
    incoming = await reader.read()
    message = parse_message(incoming.decode('ascii'))
    response = await server.handle_message(message)
    encoded = encode_response(response)
    writer.write(encoded)
    writer.write_eof()
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handler, 'localhost', 8080)
    addr = server.sockets[0].getsockname()
    print(f'listening on {addr}')
    async with server:
        await server.serve_forever()

asyncio.run(main())

