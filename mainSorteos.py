import json

clients_db = {}


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

        case 3:
            # comb generator

        case 4:
            # ticket generator
        case 5:
            # Loto 
        case 6:
            # check winners
        case 7:
            print("Goodbye".center(100,"~"))
            break