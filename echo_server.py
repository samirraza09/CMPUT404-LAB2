import socket

BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break

        print(data)
        conn.sendall(data)

    return 


def start_server():

    #Auto closes socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))

        # Allows socket to be reboundable to address
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen()

        # Accept an incoming connection. Returns a connection and it's address
        conn, addr = s.accept()

        handle_connection(conn, addr)

    return

start_server()