try:
    CONSTANTE1 = 10
    CONSTANTE2 = 100
    numero = int(input("ingrese un numero:\n"))
    print("---------------------------\n")
    unidad = numero % CONSTANTE1
    decena = ((numero % CONSTANTE2) - unidad) // CONSTANTE1
    centena = numero//CONSTANTE2
    print("---------resultado---------\n")
    print("el numero de la unidad es:", unidad)
    print("el numero en decena es:", decena)
    print("el numero en centena es:", centena)
    print("---------------------------\n")
except ValueError:
    print("el error esta en el numero ingresado:")
    print("---------------------------\n")

