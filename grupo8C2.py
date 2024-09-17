try:
    PESOPAYASO = 112
    PESOMUNECA = 75

    cantidadPayasoV = int(input("ingrese la cantidad de payasos vendidos:"))
    cantidadMunecaV = int(input("ingrese la cantidad de muñecas vendidas: "))
    totalVendidos = int(cantidadPayasoV) + int(cantidadMunecaV)
    totalPeso = (cantidadPayasoV*PESOPAYASO)+(cantidadMunecaV*PESOMUNECA)
    print("___________________________________________")
    print("el peso total del paquete es: ", totalPeso)
    print("___________________________________________")
except ValueError:
    print("porfavor ingrese un numero😁")
