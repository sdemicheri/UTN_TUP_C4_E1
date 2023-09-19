"""Colazo Fernando
   Guía 8
   Ejercicio 2

Mostrar todos los numeros impares menores de 100"""

try:
    for i in range(1,100,2):
        print(i)
except ValueError:
    print("Ingrese in valor numérico entero")