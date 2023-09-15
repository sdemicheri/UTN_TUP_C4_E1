"""Colazo Fernando
   Guía 7
   Ejercicio 6"""
try:
    renta = float(input("Ingrese el valor de su renta para saber el tipo impositivo que le corresponde: "))
    if renta < 0:
        print("Ingrese un monto mayor o igal a 0")
    elif renta < 100000:
        print("El tipo impositivo que le corresponde es de 5%", "\nSu monto sería de",renta*0.05)
    elif 100000 <= renta <= 200000:
        print("El tipo impositivo que le corresponde es de 15%", "\nSu monto sería de",renta*0.15)
    elif 200000 < renta <= 350000:
        print("El tipo impositivo que le corresponde es de 20%", "\nSu monto sería de",renta*0.20)
    elif 350000 < renta <= 600000:
        print("El tipo impositivo que le corresponde es de 30%", "\nSu monto sería de",renta*0.30)
    elif renta > 600000:
        print("El tipo impositivo que le corresponde es de 45%", "\nSu monto sería de",renta*0.45)

except ValueError:
    print("Ingrese un valor numerico mayor a 0")