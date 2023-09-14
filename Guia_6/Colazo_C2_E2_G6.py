"""Colazo Fernando
   Guía 6
   Ejercicio 2"""

"""Escriba un programa que le pida al usuario dos números y muestre por pantalla su división.
Si el divisor es 0 el programa debe mostrar un error"""

try:
    n1 = int(input("Ingrese un número a dividir: "))
    n2 = int(input("Ingrese el número por el que desea dividirlo: "))
    if n2 == 0:
        print("Ingrese un valor diferente de 0 en el divisor ")
    else:
        division = n1 / n2
        print("El resultado de su división es de: ", division)
except ValueError:
    print("Ingrese un valor numerico correcto")