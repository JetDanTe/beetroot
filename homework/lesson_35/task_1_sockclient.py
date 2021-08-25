import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65434        # The port used by the server
if __name__ == '__main__':

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = ''
        while data!='CLOSE':
            s.sendall((input("Что шлем?\n")).encode())
            data = s.recv(1024).decode()
            print(data)

    print('DONE')