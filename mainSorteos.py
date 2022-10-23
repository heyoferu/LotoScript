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

def priceChecker(size_ticket):
    match size_ticket:
        case 6:
            return 15
        case 7:
            return 105
        case 8:
            return 420
        case 9:
            return 1260
        case 10:
            return 3150

def genTicket():
    print("Generando boleto".center(100,"_"))
    print("se usaran los siguientes datos...".center(100))
    id_rfc = input("RFC del cliente:\t")
    f = open('data_base.json','r')
    a = f.read()
    db = json.loads(a)
    size = len(db[id_rfc]['ticket'])


    print(f"RFC:\t{id_rfc}")
    print(f"Nombre(s):\t{db[id_rfc]['c_name']}")
    print(f"Apellido(s):\t{db[id_rfc]['c_lname']}")
    print(f"No. de combinaciones:\t{size}")
    print(f"Precio del boleto:\t{priceChecker(size)}")

    print(f"\nSu boleto se guardo en el archivo {id_rfc}.txt para que pueda imprimirlo")

    crear = open(f"{id_rfc}.txt", "w")#Se abre el archivo
    crear.write("*------*".center(55," ")  + "\n")
    crear.write("SORTEO".center(55, " ") + "\n")
    crear.write("*------*".center(55," ")  + "\n")
    crear.write("\n")
    crear.write("Fecha: 25/10/2022" + "Hora: 10:00".center(57, " ") + "\n")
    crear.write("\n")
    crear.write("+---+".center(55," ")  + "\n")
    crear.write("|RFC|".center(55, " ") + "\n")
    crear.write("+---+".center(55," ")  + "\n")
    crear.write(str(id_rfc).center(55, " ") + "\n")
    crear.write("\n")
    crear.write("+------+".center(55," ")  + "\n")
    crear.write("|NOMBRE|".center(55, " ") + "\n")
    crear.write("+------+".center(55," ")  + "\n")
    crear.write(str(db[id_rfc]['c_name']) + str(db[id_rfc]['c_lname']).center(55, " ") + "\n")
    crear.write("\n")
    crear.write("+--------------+".center(55," ")  + "\n")
    crear.write("|No.Combinacion|".center(55, " ") + "\n")
    crear.write("+--------------+".center(55," ")  + "\n")
    crear.write(str(size).center(55, " ") + "\n")
    crear.write("\n")
    crear.write("+---------+".center(55," ")  + "\n")
    crear.write("|No.Sorteo|".center(55, " ") + "\n")
    crear.write("+---------+".center(55," ")  + "\n")
    crear.write(str(db[id_rfc]["ticket"]).center(55, " ") + "\n")
    crear.write("\n")
    crear.write("+-----+".center(55," ")  + "\n")
    crear.write("Precio".center(55, " ") + "\n")
    crear.write("+-----+".center(55," ")  + "\n")
    crear.write(str(priceChecker(size)).center(55, " ") + "\n")
    f.close()
    crear.close() #Se cierra el archivo creado

def genLoto():
    print("Generando sorteo".center(100,"_"))

    numbers = "0123456789"
    size = int(input("Introduzca el tamaño del boleto ganandor (min. 6 | max. 10):\t"))

    count_limit = 0
    while True:
        temp = "".join(random.sample(numbers,2))
        if int(temp) < 59:
            winner_ticket.append(int(temp))
            count_limit += 1
            if count_limit == size:
                break
            else:
                continue
        else:
            continue
    print(str(winner_ticket))

def ticketChecker():
    print("Validando boleto".center(100,"_"))
    size = int(input("Introduzca el tamaño del boleto ganandor (min. 6 | max. 10):\t"))
    ticket_temp = input("Inserte sus numeros separados por comas:\t")
    ticket_to_check = ticket_temp.split(',')
    
    count_limit = 0
    for number in range(size):
        if ticket_to_check[number] == winner_ticket[number]:
            count_limit += 1
    if count_limit == size:
        print(f"{ticket_to_check} es ganador")
    else:
        print(f"{ticket_to_check} no es ganador")


print("SORTEOS APP".center(100,"="))
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
            combRandom() # comb generator

        case 4:
            genTicket()# ticket generator
        case 5:
            genLoto() # Loto 
        case 6:
            ticketChecker() # check winners
        case 7:
            print("Goodbye".center(100,"~"))
            break