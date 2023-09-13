try:
    dividendo = float(input("Introduce el dividendo: "))
    divisor = float(input("Introduce el divisor: "))
    resultado = dividendo / divisor
    cociente = dividendo // divisor
    resto = dividendo % divisor
    print("El resultado es:", resultado)
    print("El cociente es", cociente)
    print("El resto es", resto)

except ZeroDivisionError:
    print("Imposible dividir entre cero")

except ValueError:
    print("Error! Debes ingresar un número valido.")
