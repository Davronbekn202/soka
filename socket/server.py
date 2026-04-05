import socket
from socket.router import handel_request

HOST = "127.0.0.1"
PORT = 8080

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Server running on http://{HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        request = client_socket.recv(4096)
        response = handel_request(request)
        # print(response)
        client_socket.sendall(response.encode())
        client_socket.close()

if __name__ == '__main__':
    start_server()