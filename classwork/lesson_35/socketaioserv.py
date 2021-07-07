import asyncio
import socket
import threading

PORT = 65434

async def handle_conn(client, addr):
    print(client, addr)
    loop = asyncio.get_event_loop()
    dat = ''
    while dat!='.':
        await loop.sock_sendall(client, (f"{addr} PONG " + dat.upper()).encode())
        dat = (await loop.sock_recv(client,1024)).decode()

    await loop.sock_sendall(client, "CLOSE".encode())
    client.close()

async def main():
    # Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', PORT))
    server.listen(8)
    server.setblocking(False)

    loop = asyncio.get_event_loop()
    while True:
        connection, client_address = await loop.sock_accept(server)
        print("New connection from ", client_address)
        loop.create_task(handle_conn(connection, client_address))


async def handle_cb(rdr, wrtr):
    dat = ''
    while dat != '.':
        wrtr.write(dat.encode())
        await wrtr.drain()
        dat = (await rdr.read(1024)).decode().upper()
    wrtr.write("CLOSE".encode())
    await wrtr.drain()


async def main2():
    serv = await asyncio.start_server(handle_cb, 'localhost', PORT)
    async with serv:
        await serv.serve_forever()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())