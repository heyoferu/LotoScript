""" Loto App """
## librerias para generar aleatorios y trabajar con json
import json
import random

client = {} # Dict que almacena clientes con la clave $RFC como un dict y dentro nombres, apellidos como strings y ticker a una lista 
winner_ticket = []  # Combinacion ganadora
ticket = [] # Combinacion (temporal) para comparar con winner_ticket


def update_db(rfc): # funcion que actualiza y agrega datos al diccionario 
    filename = rfc

    # los siguientes son en relacion a la salida de dict --> json
    jsonfile = open(f"client_data/{filename}.json","w") # json en modo de escritura
    json_temp = json.dumps(client[rfc]) # json.dumps proporciona una estructura json como strings y se almacena en una variable temporal
    jsonfile.write(json_temp) # enviamos a json_temp fuera en el archivo
    jsonfile.close() # importante cerrar el archivo

def showMenu(): # Muestra las opciones displonibles
    menu = ["Capturar cliente","Registrar combinancion","Generar combinacion aleatoria","Generar boleto","Generar sorteo","Validar boleto","Salir"]
    for option in range(len(menu)):
            print(f"({option+1}) {menu[option]}")

def addClient(): # Funcion que añade clientes al dict client

    print("Capturarando cliente".center(100,"_"))
    id_rfc = input("RFC del cliente:\t")
    names = input("Nombre(s) del cliente:\t")
    lnames = input("Apellido(s) del cliente:\t")

    client[id_rfc] = {}
    client[id_rfc]["c_name"] = names
    client[id_rfc]["c_lname"] = lnames
    update_db(id_rfc) # llamando a la funcion para redireccionar al json


def combRegister(): # registra combinaciones a eleccion del usuario

    print("Registrando combinacion".center(100,"_"))
    # ejecutar siempre como verdadero
    while True:
        size_comb = int(input("Introduzca el tamaño de sus combinacion (min. 6 | max. 10):\t")) # determina el numero de combinaciones
        comb = input("Inserte sus numeros separados por comas:\t")
        comb_list = comb.split(',') # combierte el string a lista a partir de las comas

        count_limit = 0  # contador que recibe 1 si hay numeros mayores al 59, puede usarse False y True en lugar de un sumador

        for number in range(size_comb): # revisar 1 por 1 si hay numeros mayores a 59
            if int(comb_list[number]) > 59:
                count_limit += 1 # añadir 1 al contador si los hay

        if count_limit == 0: # si no hay ninguno se mantiene en 0 y la lista de combinaciones se envia a ticket
            ticket = comb_list # ticket igual a la combinacion insertada
            print(str(ticket))
            id_rfc = input("RFC del cliente del boleto:\t") # insertar el rfc para añadir el ticket al usuario deseado
            client[id_rfc]['ticket'] = ticket
            update_db(id_rfc) # actualizar db
            break # romper el ciclo para terminar
        else:
            print("Su combinacion tiene numeros mayores a 59")
            continue # continuar si count_limit es mayor a 0

def combRandom(): # generador de combinaciones aleatorias
    print("Generando combinacion aleatoria".center(100,"_"))
    numbers = "0123456789" # numeros que puede tomar nuestro generador
    size = int(input("Introduzca el tamaño de sus combinacion (min. 6 | max. 10):\t")) # numeros de combinaciones

    count_limit = 0 # 

    while True: # se ejecuta siempre
        temp = "".join(random.sample(numbers,2)) # generar un numero de 2 digitos 
        if int(temp) < 59: # si es menor a 59 añadirlo al ticket
            ticket.append(int(temp))
            count_limit += 1 # sumar 1 a count_limit para indicar que un espacio del tamaño total de numeros se ha llenado
            if count_limit == size:
                """
                si Count limit llega al mismo valor de numero de combinaciones
                entonces eso indica que se han encontrado n numeros menores a 59 y han sido añadidos al ticket
                """
                print(str(ticket))
                id_rfc = input("RFC del cliente del boleto:\t") # enviar el ticket al rfc del cliente
                
                client[id_rfc]['ticket'] = ticket
                update_db(id_rfc)
                break
            else:
                # si no aun seguir ejecutando 
                continue
        else: # continuar con el while aun, se entiende que algunos numeros si son mayores a 59 no se cumple el if entonces sigue buscando hasta encontrar
            continue

def priceChecker(size_ticket): # determina el precio con el n numero de combinaciones
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

def genTicket(): # generar un boleto y lo manda a un archivo externo

    print("Generando boleto".center(100,"_"))
    print("se usaran los siguientes datos...".center(100))
    # Se indica el rfc para obtener los datos a imprimir
    id_rfc = input("RFC del cliente:\t")

    # se abre el archivo json en modo lectura para extraer la informacion del objeto
    f = open(f'client_data/{id_rfc}.json','r')
    a = f.read()
    db = json.loads(a) # loads carga lo que f.read esta leyendo del json
    size = len(db['ticket']) # determina el tamaño del billete para imprimir el precio


    print(f"RFC:\t{id_rfc}")
    print(f"Nombre(s):\t{db['c_name']}")
    print(f"Apellido(s):\t{db['c_lname']}")
    print(f"No. de combinaciones:\t{size}")
    print(f"Precio del boleto:\t{priceChecker(size)}")

    print(f"\nSu boleto se guardo en el archivo {id_rfc}.txt para que pueda imprimirlo")

    crear = open(f"client_ticket/{id_rfc}.txt", "w")#Se abre el archivo
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
    crear.write(str(db['c_name']) + str(db['c_lname']).center(55, " ") + "\n")
    crear.write("\n")
    crear.write("+--------------+".center(55," ")  + "\n")
    crear.write("|No.Combinacion|".center(55, " ") + "\n")
    crear.write("+--------------+".center(55," ")  + "\n")
    crear.write(str(size).center(55, " ") + "\n")
    crear.write("\n")
    crear.write("+---------+".center(55," ")  + "\n")
    crear.write("|No.Sorteo|".center(55, " ") + "\n")
    crear.write("+---------+".center(55," ")  + "\n")
    crear.write(str(db["ticket"]).center(55, " ") + "\n")
    crear.write("\n")
    crear.write("+-----+".center(55," ")  + "\n")
    crear.write("Precio".center(55, " ") + "\n")
    crear.write("+-----+".center(55," ")  + "\n")
    crear.write(str(priceChecker(size)).center(55, " ") + "\n")
    f.close()
    crear.close() #Se cierra el archivo creado

def genLoto(): # generar sorteo
    print("Generando sorteo".center(100,"_"))

    """
        Al igual que en el generador de boletos, genLoto, genera una combinacion
        de n 10 numeros de 2 digitos, y revisa que no sean mayores al limite para 
        agregarlos a la variable que almacena el boleto ganador
    """
    numbers = "0123456789" # numeros para crear combinaciones
    size = int(input("Introduzca el tamaño del boleto ganandor (min. 6 | max. 10):\t")) # tamaño de combinaciones

    count_limit = 0 # para igualar con size
    while True:
        # generar combinaciones de 2 digitos de 1 en 1
        temp = "".join(random.sample(numbers,2))
        if int(temp) < 59: # si es menor a 59 añadir a winner_ticket            winner_ticket.append(int(temp))
            count_limit += 1 # sumar 1 al contador para indicar que un numero se ha añadido
            if count_limit == size:
                # si han añadido la misma cantidad de numeros que indica size entonces romper el ciclo
                break
            else:
                continue
        else:
            continue
    print(str(winner_ticket))

def ticketChecker():

    # Funcion que validad si el ticker es ganador, o sea, igual a winner_ticket
    print("Validando boleto".center(100,"_"))
    size = int(input("Introduzca el tamaño del boleto ganandor (min. 6 | max. 10):\t")) # no. de combinaciones
    ticket_temp = input("Inserte sus numeros separados por comas:\t")
    ticket_to_check = ticket_temp.split(',')
    
    count_limit = 0 # contador de veces que se hayaron coicidencias
    for number in range(size):
        if ticket_to_check[number] == winner_ticket[number]:
            count_limit += 1
    if count_limit == size: # si todos los numeros de ticket y de winner ticket son iguales, el boleto es igual y es ganador
        print(f"{ticket_to_check} es ganador")
    else:
        print(f"{ticket_to_check} no es ganador")



# Menu que llama a las funciones anteriormente declaradas
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
        case 7: # exit or kill session
            print("Goodbye".center(100,"~"))
            break