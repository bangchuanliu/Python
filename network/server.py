import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
LEN = 64
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    while True:
        msg_length = conn.recv(LEN).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == "DISCONNECTED":
                break
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

print("[STRATING] server is starting... ")
start()


