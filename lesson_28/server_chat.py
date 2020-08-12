import asyncio
from typing import Any, Optional


class MySeverChat(asyncio.Protocol):

    def __init__(self, loop, clients):
        self.msg = []
        self.message = None
        self.clients = clients
        self.loop = loop
        self.now_client = None
        self.peername = None

    def connection_lost(self, exc: Optional[Exception]) -> None:
        try:
            self.clients.remove(self.now_client)
        except:
            pass

    def connection_made(self, client) -> None:
        self.peername = client.get_extra_info('peername')
        print(f'connection : {self.peername}')
        self.now_client = client
        self.clients.append(self.now_client)
        self.send()

    def data_received(self, data: bytes) -> None:
        self.message = f'{self.peername[1]}: {data.decode()}\n'
        self.msg.append(f'{self.peername[1]}: {data.decode()}\n')
        print(*self.msg)
        self.send()

    def send(self):
        for client in self.clients:
            if client == self.now_client:
                for msg in self.msg:
                    client.write(bytes(msg, encoding='utf-8'))
            else:
                client.write(bytes(self.message, encoding='utf-8'))


def main():
    clients = []
    loop = asyncio.get_event_loop()
    coro = loop.create_server(lambda: MySeverChat(loop, clients), '127.0.0.1', 8888)
    server = loop.run_until_complete(coro)
    print(f'Serving on {(server.sockets[0].getsockname())}')
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    main()
