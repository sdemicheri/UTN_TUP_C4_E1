def calcular_promedio(nota1, nota2, nota3):
    suma = nota1 + nota2 + nota3
    promedio = suma // 3  # Usamos la división entera para obtener un resultado entero
    return promedio


nota1 = int(input("Ingrese la primera nota parcial: "))
nota2 = int(input("Ingrese la segunda nota parcial: "))
nota3 = int(input("Ingrese la tercera nota parcial: "))


promedio = calcular_promedio(nota1, nota2, nota3)


print("El promedio simple de las 3 notas parciales es:", promedio)
