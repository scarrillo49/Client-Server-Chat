# server.py
import socket
from threading import Thread
import random

host = "127.0.0.1"
port = 6460

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def generate_random_nickname():
    return f"Client-{random.randint(1, 1000)}"


def broadcast(message):
    for client in clients:
        try:
            client.send(f"{message}".encode("ascii"))
        except (BrokenPipeError, ConnectionError):
            handle_client_disconnection(client)


def receive():
    while True:
        client, address = server.accept()
        

        nickname = client.recv(1024).decode("ascii")

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}!")

        broadcast(f"{nickname} joined the chat.")
        client.send("Connected to the server!".encode("ascii"))

        t = Thread(target=handle, args=(client, nickname))
        t.start()


def handle(client, nickname):
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message.endswith(": .exit"):
                handle_exit(client, nickname)
                break
            else:
                broadcast(message)
        except (BrokenPipeError, ConnectionError):
            handle_client_disconnection(client)
            break


def handle_exit(client, nickname):
    clients.remove(client)
    nicknames.remove(nickname)
    broadcast(f"{nickname} has left the chat.")
    client.send("Exit confirmed".encode("ascii"))
    client.close()


def handle_client_disconnection(client):
    if client in clients:
        nickname_index = clients.index(client)
        nickname = nicknames[nickname_index]
        clients.remove(client)
        nicknames.remove(nickname)
        broadcast(f"{nickname} has left the chat.")
        

if __name__ == "__main__":
    print("Server is listening...")
    receive()