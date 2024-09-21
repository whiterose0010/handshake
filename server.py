import socket
import threading

clients = []

def handle_client(client_socket, addr):
    print(f"New Connection : {addr}")
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(4096).decode()
            if not message:
                break
            broadcast(message, client_socket)
        except Exception as e:
            print(f"Error : {e}")
            break

    client_socket.close()
    clients.remove(client_socket)
    print(f"Connection closed : {addr}")

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)


def server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Chat server started on {host} : {port}")

    while True:
        client_socket, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

if __name__=='__main__':
    host = input('Masukkan alamat host : ')
    port = int(input('Masukkan port : '))
    server(host, port)            
