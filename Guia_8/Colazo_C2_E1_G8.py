"""Colazo Fernando
   Guía 8
   Ejercicio 1

Escribir un programa que calcule el promedio de una cantidad x de números ingresados"""

try:
    cant = int(input("Ingrese la cantidad de números a la que le desea hacer el promedio: "))
    print("Ahora ingrese los numeros de a uno cuando se lo pida")
    acu = 0
    for i in range(cant):
        num = int(input("Ingrese un número: "))
        acu = acu + num
    promedio = acu/cant
    print("El promedio de los números ingresados es",promedio)
except ValueError:
    print("Ingrese in valor numérico entero")