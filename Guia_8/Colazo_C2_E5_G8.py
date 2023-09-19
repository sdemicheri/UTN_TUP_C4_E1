"""Colazo Fernando
   Guía 8
   Ejercicio 5

Escribir un programa que muestre el eco de todo lo que el usuario introduzca hastq que
el usuario escriba salir"""

frase = " "
while frase != "salir":
        frase = input("Ingrese lo que quiera y yo lo repitiré: ")
        print(frase)