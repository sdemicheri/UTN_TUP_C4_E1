"""Colazo Fernando
   Guía 8
   Ejercicio 7

Datos:
      x= cantidad de botellas que se necesitan para fabricar otra (pedirlo)
      n= caqntidad de boteellas que tenemos (pedirlo)

Entrada: x y n
Salida: La cantidad total acumulada de botellas que pueden fabricarse a partir
 de N botelas, reciclandolas repetidamente hasta que no queden suficientes botellas """
try:
    n = int(input("Ingrese la cantidad de botellas disponibles: "))
    x = int(input("Ingrese la cantidad de botellas que se necesitan para fabricar otra: "))
    ntotal = n
    acu = 0
    sobrante = 0
    if n/x == n:
        print("A partir de", ntotal, "botellas del mercado, pueden fabricarse: ", n, " botellas recicladas.")
        print("Y sobran", sobrante, "botellas del mercado")
    else:
        while n/x >= 1:
            sobrante = n % x
            n = n // x
            acu = acu + n
            n = n + sobrante
        print("A partir de", ntotal, "botellas del mercado, pueden fabricarse: ", acu, " botellas recicladas.")
        print("Y sobran", sobrante, "botellas del mercado")
except ValueError:
    print("Ingrese un número entero válido")
