DIRECCION = 'Clinica abcde - calle: Av. aeiou 123'

nombre = input('Ingrese el nombre del paciente: ') 
fecha_nac = input('Ingrese fecha de nacimiento (DD/MM/AAAA): ')
medicamento = input('Indique nombre del medicamento recetado: ')
dosis = input('Indique la dosis recetada: ')
prox_turno = input('Indique fecha del proximo turno (DD/MM/AAAA): ')
horario = input('Indique horario del proximo turno: ')

def imprimirReceta():
    print('*' * 70)
    print(f'Nombre y Apellido: {nombre}').center()
    print(f'Fecha de nacimiento: {fecha_nac}')
    print(f'Medicamento recetado: {medicamento}')
    print(f'Dosis: {dosis}')
    print(f'Proximo truno: {prox_turno}, {horario}hs')
    print(DIRECCION)
    print('*' * 70)
    

imprimirReceta()
