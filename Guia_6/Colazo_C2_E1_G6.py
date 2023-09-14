"""Colazo Fernando
   Guía 6
   Ejercicio 1"""

#Escriba un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no

try:
    edad = int(input("Ingrese su edad: "))
    if edad >=18 and  edad > 0:
        print("Es mayor de edad")
    elif edad < 0:
        print("Ingrese una edad correcta")
    else:
        print("Es menor de edad")
except ValueError:
    print("Ingrese un valor numerico correcto")