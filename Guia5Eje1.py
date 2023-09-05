# Ingresa el precio, inflacion y los años y le calcula el precio basado en la inflacion

c, r = float(input("Ingrese el precio del objeto\n")), float(input("Ingrese la inflacion anualizada\n"))
a, n = float(input("Ingrese el año actual\n")), float(input("Ingrese el año de estudio\n"))
p = c*((1+r/100)**(n-a))
print(p)
