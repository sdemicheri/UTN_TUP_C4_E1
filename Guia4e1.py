try:
    edad = int(input("📆 Ingrese su edad: "))

    if edad >= 18:
        print("🙋‍♂️ Eres mayor de edad")
    elif edad <= 0:
        print("❌ Ingrese un número valido.")
    elif edad < 18:
        print("👦 No eres mayor de edad")

except ValueError:
    print("❌ Ingrese un número valido.")
