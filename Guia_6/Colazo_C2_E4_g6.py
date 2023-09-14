"""Colazo Fernando
   Guía 6
   Ejercicio 4"""

"""Ingresar un número del 1 al 10 y escribir sus correspondiente en letras"""

try:
    n = int(input("Ingrese un número del 1 al 10: "))
    if n == 1:
        print("El número indicado es el: uno")
    elif n == 2:
        print("El número indicado es el: dos")
    elif n == 3:
        print("El número indicado es el: tres")
    elif n == 4:
        print("El número indicado es el: cuatro")
    elif n == 5:
        print("El número indicado es el: cinco")
    elif n == 6:
        print("El número indicado es el: seis")
    elif n == 7:
        print("El número indicado es el: siete")
    elif n == 8:
        print("El número indicado es el: ocho")
    elif n == 9:
        print("El número indicado es el: nueve")
    elif n == 10:
        print("El número indicado es el: diez")
    else:
        print("Inngre un número entre 1 y 10, ni mayor ni menor")
except ValueError:
    print("Ingrese un valor numerico correcto")