def es_divisible(numero, divisor):
    if numero % divisor == 0:
        return True
    else:
        return False


numero = int(input("Ingrese el número: "))
divisor = int(input("Ingrese el divisor: "))


if es_divisible(numero, divisor):
    print(f"{numero} es divisible por {divisor}.")
else:
    print(f"{numero} no es divisible por {divisor}.")