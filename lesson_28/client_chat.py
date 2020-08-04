import asyncio


async def my_client(loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888, loop=loop)


    print('your message ')
    msg = input('> ').strip()
    writer.write(msg.encode())


client_loop = asyncio.get_event_loop()
client_loop.run_until_complete(my_client(client_loop))
client_loop.run_forever()
client_loop.close()