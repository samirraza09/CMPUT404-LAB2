import socket

BYTES_TO_READ = 4096

def get(host, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(( host, port ))

    request_data = b"GET / HTTP/1.1\nHost:" + host.encode("utf-8") + b"\n\n" #Converting to bytes
    s.send(request_data)
    
    s.shutdown(socket.SHUT_WR)
    result = s.recv(BYTES_TO_READ)
    while(len(result) > 0):
        print(result)
        result = s.recv(BYTES_TO_READ)

    s.close()

get("www.google.com", 80)
