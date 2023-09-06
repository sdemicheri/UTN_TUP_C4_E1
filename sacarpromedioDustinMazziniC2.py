def calcular_promedio(n1, n2, n3, n4):
    suma = n1 + n2 + n3 + n4
    promedio = suma // 4
    return promedio


n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))
n4 = int(input("Ingrese el cuarto número: "))


promedio = calcular_promedio(n1, n2, n3, n4)


print("El promedio de los cuatro números es:", promedio)