"""Colazo Fernando
   Guía 7
   Ejercicio 2

En un almacén se rebaja 10% del precio al cliente si compra mas de 20 artículos y 5% si
compra hasta 20 artículos pero más de 10. Dado el precio unitario de un artículo y la cantidad
adquirida, muestre lo que debe pagar el cliente."""

try:
    precio_unitario = float(input("Ingrese el precio del artículo: "))
    cantidad_arti = int(input("Ingrese la cantidad de articulos: "))
    if cantidad_arti > 20:
        total = cantidad_arti*precio_unitario*0.9
        print("El precio por los ", cantidad_arti, "es de: $",total )
    elif cantidad_arti < 20 and cantidad_arti > 10:
        total = cantidad_arti*precio_unitario*0.95
        print("El precio por los ", cantidad_arti, "es de: $", total)
    else:
        total = cantidad_arti*precio_unitario
        print("El precio por los ", cantidad_arti, "es de: $",total )
except ValueError:
    print("Ingrese un valor numerico correcto")