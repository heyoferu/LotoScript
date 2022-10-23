import json
import random

clients_db = {}
winner_ticket = []
ticket = []


def update_db():
    jsonfile = open("data_base.json","w")
    json_temp = json.dumps(clients_db)
    jsonfile.write(json_temp)
    jsonfile.close()

def showMenu():
    menu = ["Capturar cliente","Registrar combinancion","Generar combinacion aleatoria","Generar boleto","Generar sorteo","Validar boleto","Salir"]
    for option in range(len(menu)):
            print(f"({option+1}) {menu[option]}")

def addClient():
    print("Capturarando cliente".center(100,"_"))
    id_rfc = input("RFC del cliente:\t")
    names = input("Nombre(s) del cliente:\t")
    lnames = input("Apellido(s) del cliente:\t")

    clients_db[id_rfc] = {}
    clients_db[id_rfc]["c_name"] = names
    clients_db[id_rfc]["c_lname"] = lnames
    update_db()


def combRegister():
    print("Registrando combinacion".center(100,"_"))
    while True:
        size_comb = int(input("Introduzca el tamaño de sus combinacion (min. 6 | max. 10):\t"))
        comb = input("Inserte sus numeros separados por comas:\t")
        comb_list = comb.split(',')

        count_limit = 0

        for number in range(size_comb):
            if int(comb_list[number]) > 59:
                count_limit += 1

        if count_limit == 0:
            ticket = comb_list
            print(str(ticket))
            id_rfc = input("RFC del cliente del boleto:\t")
            clients_db[id_rfc]['ticket'] = ticket
            update_db()
            break
        else:
            print("Su combinacion tiene numeros mayores a 59")
            continue

def combRandom():
    print("Generando combinacion aleatoria".center(100,"_"))
    numbers = "0123456789"
    size = int(input("Introduzca el tamaño de sus combinacion (min. 6 | max. 10):\t"))

    count_limit = 0
    while True:
        temp = "".join(random.sample(numbers,2))
        if int(temp) < 59:
            ticket.append(int(temp))
            count_limit += 1
            if count_limit == size:
                print(str(ticket))
                id_rfc = input("RFC del cliente del boleto:\t")
                clients_db[id_rfc]['ticket'] = ticket
                update_db()
                break
            else:
                continue
        else:
            continue


print("SORTEOS DEL BIENESTAR".center(100,"="))
while True:

    showMenu() # menu here

    select_option = int(input("Seleccione una opcion:\t"))
    match select_option:
        case 1:
            # clients register 
            addClient()
        case 2:
            # comb register
            combRegister()

        case 3:
            # comb generator
            combRandom()

        case 4:
            # ticket generator
        case 5:
            # Loto 
        case 6:
            # check winners
        case 7:
            print("Goodbye".center(100,"~"))
            break