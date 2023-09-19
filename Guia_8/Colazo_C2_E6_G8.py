"""Colazo Fernando
   Guía 8
   Ejercicio 6

   Entrada: el código ISBN
   Datos:
   -El codigo ISBN, no lo tengo debo pedirlo
   -Residuo: s/11
   -S: la suma de los primeros 9 digitos por su posicion
   Salida: Decir si el código ISBN fue escrito correctamente para eso el residuo debe ser igual al
   último digito del código ISBN
   """
try:
    print("Determinar si el ISBN está bien escrito")
    codigo = int(input("Ingrese el código ISBN correspondiente: "))
    a2 = 10000000000
    a1 = 1000000000
    acu = 1
    s = 0
    for i in range(9):
        n = (codigo % a2) // a1
        s = n * acu + s
        a1 = a1 // 10
        a2 = a2 // 10
        acu = acu + 1
    if s % 11 == codigo % 10:
        print("El código ISBN: ", codigo, " está escrito correctamente")
    else:
        print("El código ISBN: ", codigo, " no está escrito correctamente")
except ValueError:
    print("Ingrese un valor numérico entero de 10 digitos")



