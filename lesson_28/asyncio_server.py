import asyncio


async def my_server(reader, writer):
    data = await reader.read(1024)
    msg = data.decode()
    add = writer.get_extra_info('peername')
    print(f'received : {msg} from {add}')
    writer.close()

server_loop = asyncio.get_event_loop()
server_aio = asyncio.start_server(my_server, '127.0.0.1', 65000, loop=server_loop)
server_work = server_loop.run_until_complete(server_aio)

try:
    server_loop.run_forever()
finally:
    server_work.close()
    server_loop.run_until_complete(server_work.wait_closed())
    server_loop.close()