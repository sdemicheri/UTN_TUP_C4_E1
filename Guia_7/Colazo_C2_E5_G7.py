"""Colazo Fernando
   Guía 7
   Ejercicio 5

Ingrese tres números correspondientes a un conjunto y tres números correspondientes a otro conjunto.
Muestre los números que corresponden a la intersección de los dos conjuntos. Sugerencia: Usa una
variable para cada elemento del conjunto
-conjunto A = (457]
-conjunto B = [279]
-intersección AnB=7"""
"""No se si entendí bien la consigna aunque me quedaron dudas para saber como 
hacer si hay dos número de intersección"""

A1 = 4
A2 = 5
A3 = 7
B1 = 2
B2 = 7
B3 = 9

    if A1 == B1 or A1 == B2 or A1 == B3:
        print("La intersección entre el conjunto A y el B es: ", A1)
    if A2 == B1 or A2 == B2 or A2 == B3:
        print("La intersección entre el conjunto A y el B es: ", A2)
    if A3 == B1 or A3 == B2 or A3 == B3:
        print("La intersección entre el conjunto A y el B es: ", A3)
    else:
        print("No tiene intersección")

