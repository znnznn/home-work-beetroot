import asyncio
from typing import Any, Optional


class MySeverChat(asyncio.Protocol):
    msg = []

    def __init__(self, loop, clients):
        self.message = ''
        self.clients = clients
        self.loop = loop
        self.new_client = False
        self.now_client = None
        self.peername = None

    def connection_lost(self, exc: Optional[Exception]) -> None:
        try:
            self.clients.remove(self.now_client)
            self.message = f'Exit chat: {self.peername[1]}'
            self.send()
        except:
            pass

    def connection_made(self, client) -> None:
        self.peername = client.get_extra_info('peername')
        print(f'connection : {self.peername}')
        self.now_client = client
        if self.now_client not in self.clients:
            self.clients.append(self.now_client)
            self.new_client = True
            self.send()

    def data_received(self, data: bytes) -> None:
        self.message = f'{self.peername[1]}: {data.decode()}\n'
        self.msg.append(self.message)
        self.send()

    def send(self):
        """ sends a message to the clients  """
        for client in self.clients:
            if client == self.now_client and self.new_client:
                message = ''.join([i for i in self.msg])
                client.write(bytes(message, encoding="utf-8"))
                self.new_client = False
            else:
                client.write(bytes(self.message, encoding="utf-8"))


def main():
    """ start server """
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
