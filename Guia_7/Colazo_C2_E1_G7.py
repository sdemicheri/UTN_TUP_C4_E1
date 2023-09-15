"""Colazo Fernando
   Guía 7
   Ejercicio 1

Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma
automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del
cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre
4 y 18 años debe pagar $500 y si es mayor de 18 años, $800 """

try:
    edad = int(input("Ingrese la edad del cliente: "))
    if edad > 0 and edad < 4 :
        print("El precio de la entrada es: $0.00")
    elif edad > 3 and edad < 19:
        print("El precio de la entrada es: $500.00")
    elif edad > 18:
        print("El precio de la entrada es: $800.00")
    else:
        print("Ingrese una edad positiva")
except ValueError:
    print("Ingrese un valor numerico entero")