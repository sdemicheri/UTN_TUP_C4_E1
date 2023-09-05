
ppc, pi = float(input("Ingrese el precio de la computadora\n")), float(input("Ingrese el precio de la impresora\n"))
gpc, gi = float(input("Ingrese el porcentage de ganancia de la computadora\n")), float(input("Ingrese el porcentage de ganancia de la impresora\n"))
gpc, gi = gpc/100, gi/100
print(ppc, pi, gpc, gi)
iva = 0.21
pf = ppc*(1+gpc)+pi*(1+gi)
print(pf)
pf = pf*(1+iva)
print(f"El costo total es de {pf}")
