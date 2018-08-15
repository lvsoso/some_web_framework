#coding=utf-8

import socket

HOST = "localhost"
PORT = 8888
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(128)
    while True:
        conn, addr = s.accept()
        print("Connected by", addr)
        with conn:
            while 1:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
