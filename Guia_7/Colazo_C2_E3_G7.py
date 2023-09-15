"""Colazo Fernando
   Guía 7
   Ejercicio 3"""

try:
    precio_kg = float(input("Ingresa el precio del kg de manzana: "))
    cantidad_kg = float(input("Ingresa la cantidad de kg de manzana que va a llevar: "))
    if cantidad_kg >= 0 and cantidad_kg <= 2:
        precio = precio_kg*cantidad_kg
        print("El costo de los", cantidad_kg,"Kg de manzana es de: $", precio)
    elif cantidad_kg > 2 and cantidad_kg <= 5:
         precio = precio_kg*cantidad_kg*0.9
         print("El costo de los", cantidad_kg,"Kg de manzana es de: $", precio)
    elif cantidad_kg > 5 and cantidad_kg <= 10:
         precio = precio_kg*cantidad_kg*0.85
         print("El costo de los", cantidad_kg,"Kg de manzana es de: $", precio)
    elif cantidad_kg > 10:
         precio = precio_kg*cantidad_kg*0.8
         print("El costo de los", cantidad_kg,"Kg de manzana es de: $", precio)
    else:
        print("Ingrese un número positivo")
except ValueError:
    print("Ingrese un valor númerico positivo")