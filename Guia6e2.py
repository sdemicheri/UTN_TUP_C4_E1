try:
    dividiendo = float(input("🔢 Ingrese el dividiendo: "))
    divisor = float(input("🔢 Ingrese el divisor: "))
    result = dividiendo / divisor
    print("El resultado es: ", result)
except ZeroDivisionError:
    print("❌ No puede dividir por cero!")
except ValueError:
    print("❌ Ingrese un número")


