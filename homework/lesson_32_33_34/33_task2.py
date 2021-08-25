"""Task 2

Echo server with threading

Create a socket echo server which handles each connection in a separate Thread

"""
import socket
import threading

# Create a TCP/IP socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 65433)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(10)

class H_con(threading.Thread):
    def __init__(self, connection, client_adress):
        super().__init__()
        self.connection = connection
        self.client_adress = client_adress


    def run(self):
        for i in range(100, 0, -1):
            self.connection.sendall(f"Осталось {i} секундочек...".encode())
            time.sleep(1.0)
        self.connection.close()

if __name__ == '__main__':
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        worker = H_con(connection, client_address)
        worker.start()



