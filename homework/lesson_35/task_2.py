"""Task 2

Requests using asyncio and aiohttp

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump it to a file. For this task use asyncio and
aiohttp libraries for making requests to Reddit API."""



import asyncio
import json
import socket
import threading

import aiohttp

PORT = 65123

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
        try:
            advo = await search_advo(dat)
            dat = json.dumps(advo)
        except:
            dat = "Not found"
    wrtr.write("CLOSE".encode())
    await wrtr.drain()


async def main2():
    serv = await asyncio.start_server(handle_cb, 'localhost', PORT)
    async with serv:
        await serv.serve_forever()

async def search_advo(fio: str) -> dict:
    dat = await get_fio(fio)
    async with aiohttp.ClientSession() as session:
        async with session.get('https://erau.unba.org.ua/search', params = dat ) as response:
            if response.ok:
                data = await response.json()
                if data["items"]:
                    return data['items'][0]
                else:
                    print(data)
            else:
                 print(await response.text())
    raise Exception("KERNEL PANIC")


async def get_fio(fio: str) -> dict:
    s_name = fio.strip()
    f_name, m_name = "", ""
    if fio.strip().find(" "):
        s_name, *f_name, m_name = fio.split(" ")
        f_name = " ".join(f_name)
    return {"limit": 8, "offset": 0, 'surname': s_name, 'firstname': f_name, 'middlename': m_name}

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main2())