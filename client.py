import socket
import threading

def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(4096).decode()
            if message:
                print(message)
            else:
                break
        except:
            print("Error receiving message.")
            break

def client(target_host, target_port):
    username = input("Masukkan username anda: ")
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target_host, target_port))

    threading.Thread(target=receive_message, args=(client_socket,)).start()
    while True:
        message = input ()
        if message.lower() == 'exit':
            break
        # mengirim pesan dengan username
        full_message = f"{username} : {message}"
        client_socket.send(full_message.encode())
    client_socket.close()

if __name__=='__main__':
    target_host = input('Masukkan server host : ')
    target_port = int(input('Masukkan server port : '))
    client(target_host, target_port)