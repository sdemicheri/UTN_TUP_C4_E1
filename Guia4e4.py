try:
    num = int(input("Ingrese un número del 1 al 10: "))

    match num:
        case 1:
            print("Uno")
        case 2:
            print("Dos")
        case 3:
            print("Tres")
        case 4:
            print("Cuatro")
        case 5:
            print("Cinco")
        case 6:
            print("Seis")
        case 7:
            print("Siete")
        case 8:
            print("Ocho")
        case 9:
            print("Nueve")
        case 10:
            print("Diez")
        case _:
            print("ERROR ❌ Ingrese un número del 1 al 10")

except ValueError:
    print("ERROR ❌ Ingrese un número del 1 al 10")
