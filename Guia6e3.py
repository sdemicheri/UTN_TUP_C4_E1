try:
    num = int(input("Ingrese un número entero: "))

    if num % 2 == 0:
        print(num, "es par")
    else:
        print(num, "es impar")
except ValueError:
    print("ERROR ❌ Ingrese un número valido")