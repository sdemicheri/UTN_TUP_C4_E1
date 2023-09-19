"""Colazo Fernando
   Guía 8
   Ejercicio 2

Escribir un programa que muestre los números pares que existen entre dos números ingresados"""

try:
    n1 = int(input("Ingrese un número al azar: "))
    n2 = int(input("Ingrese otro número al azar: "))
    print("Los números pares entre ", n1, " y ", n2, "son:")
    if n1 % 2 == 0 and n1<n2:
        for i in range(n1+2,n2,2):
            print(i)
    elif n1%2 != 0 and n1<n2:
        for i in range(n1+1,n2,2):
            print(i)
    elif n2 % 2 == 0 and n1 > n2:
        for i in range(n2+2,n1,2):
            print(i)
    elif n2 % 2 != 0 and n1 > n2:
        for i in range(n2+1,n1,2):
            print(i)
    else:
        print("Ingrese dos números diferentes")
except ValueError:
    print("Ingrese un valor numérico entero")