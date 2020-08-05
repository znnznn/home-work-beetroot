import asyncio
from typing import Any, Optional


class MySeverChat(asyncio.Protocol):

    def __init__(self, loop):
        self.msg = []
        self.loop = loop
        self.now_client = None
        self.client = []
        self.peername = None

    def connection_lost(self, exc: Optional[Exception]) -> None:
        try:
            self.client.remove(self.now_client)
        except:
            self.loop.stop()
        self.loop.stop()

    def connection_made(self, client) -> None:
        self.peername = client.get_extra_info('peername')
        print(f'connection : {self.peername}')
        self.now_client = client
        self.client.append(self.now_client)
        self.send()

    def data_received(self, data: bytes) -> None:
        self.msg.append(f'{self.peername}: {data.decode()}')
        print(*self.msg)
        self.send()

    def send(self):
        for client in self.client:
            for msg in self.msg:
                client.write(bytes(msg, encoding='utf-8'))




loop = asyncio.get_event_loop()
coro = loop.create_server(lambda: MySeverChat(loop), '127.0.0.1', 8888)
server = loop.run_until_complete(coro)


print(f'Serving on {(server.sockets[0].getsockname())}')
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()