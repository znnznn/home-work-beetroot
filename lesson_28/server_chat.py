import asyncio
from typing import Any, Optional


class MySeverChat(asyncio.Protocol):

    def __init__(self, loop):
        self.msg = []
        self.loop = loop
        self.now_client = None
        self.client = []

    def connection_lost(self, exc: Optional[Exception]) -> None:
        try:
            self.client.remove(self.now_client)
        except:
            self.loop.stop()
        self.loop.stop()

    def connection_made(self, client) -> None:
        peername = client.get_extra_info('peername')
        print(f'connection : {peername}')
        self.now_client = client
        self.client.append(client)

    def data_received(self, data: bytes) -> None:
        self.msg.append(data.decode())
        self.send()
        print(self.msg)


    async def send(self):
        for client in self.client:
            self.client.write(f'{client}: {self.msg}').encode()



loop = asyncio.get_event_loop()
coro = loop.create_server(lambda: MySeverChat(loop), '127.0.0.1', 8888)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print(f'Serving on {(server.sockets[0].getsockname())}')
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()