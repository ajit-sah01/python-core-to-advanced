import socket

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)
print("Server started")
