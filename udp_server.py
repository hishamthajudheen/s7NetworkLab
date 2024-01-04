import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.2", 8000)

server.bind(server_address)
print(f"Server Listening on: {server_address}")
message = 'The Server recieved your message!'

try:
    while True:
        data, client_address = server.recvfrom(1024)
        print(data.decode())
        server.sendto(message.encode(), client_address)
except KeyboardInterrupt():
    server.close()
    exit()   
