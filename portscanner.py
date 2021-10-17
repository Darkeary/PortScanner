import socket
from IPy import IP

ipaddress = input("IP: ")
port= 80

try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
    print("Succes")
except:
    pass
