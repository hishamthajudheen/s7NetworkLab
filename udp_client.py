import socket

client= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.2", 8000)

try:
    while True:
        message = input("Enter message to Server: ")
        client.sendto(message.encode(), server_address)
        data, address = client.recvfrom(1024)
        print(data.decode())
        if data.decode() == "recieved":
            break
except KeyboardInterrupt():
    client.close()
    exit()
    