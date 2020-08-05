import asyncio


class ClientChat(asyncio.Protocol):
    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print(f'Data sent: {self.message}')

    def data_received(self, data):
        print(f'Data received: {data.decode()}')

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)


async def main():
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()
    message = input('>')

    transport, protocol = await loop.create_connection(
        lambda: ClientChat(message, on_con_lost),
        '127.0.0.1', 8888)
    try:
        await on_con_lost
    finally:
        transport.close()

asyncio.run(main())
