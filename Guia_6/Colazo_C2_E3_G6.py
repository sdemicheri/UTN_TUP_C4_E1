"""Colazo Fernando
   Guía 6
   Ejercicio 3"""

"""Ingresar un número dentero y mostrar si es par o impar"""

try:
    n = int(input("Ingrese un número entero para saber si es par o impar: "))
    if n % 2 == 0 and n != 0:
        print("El número indicado es par")
    else:
        print("El número indicado es impar")
except ValueError:
    print("Ingrese un valor numerico correcto")