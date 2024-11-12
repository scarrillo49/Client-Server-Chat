# client.py
import socket
import random
import threading

def generate_random_nickname():
    return f"Client-{random.randint(1, 1000)}"


def receive():
    try:
        while True:
            message = client.recv(1024).decode("ascii")
            if message.endswith(": .exit"):
                break
            print(message)
    except (socket.error, BrokenPipeError, ConnectionResetError):
        print("Connection closed.")
    finally:
        client.close()


def send():
    try:
        while True:
            message = f"{nickname}: {input()}"
            client.send(message.encode("ascii"))
            if message.endswith(": .exit"):
                break
    except (socket.error, BrokenPipeError, ConnectionResetError):
        print("Connection closed.")
    finally:
        client.close()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 6460))

nickname = generate_random_nickname()
client.send(nickname.encode("ascii"))

receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()