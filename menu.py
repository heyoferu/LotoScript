def showMenu():
    menu = ["Capturar cliente","Registrar combinancion","Generar combinacion aleatoria","Generar boleto","Generar sorteo","Validar boleto","Salir"]
    for option in range(len(menu)):
            print(f"({option+1}) {menu[option]}")