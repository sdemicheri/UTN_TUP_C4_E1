"""Colazo Fernando
   Guía 8
   Ejercicio 4

Escribir un programa que le pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo, de altura el número introducido

*
**
***
****
"""

try:
    num = int(input("Ingrese un número entero el cual va a ser la altura del triangulo que vamos a graficar: "))
    acu = 0
    if num <= 0:
        print("Ingrese un valor mayor a 0")
    else:
        for i in range(0,num+1,1):
            print("*" * i)
except ValueError:
    print("Igrese un valor numérico entero")
