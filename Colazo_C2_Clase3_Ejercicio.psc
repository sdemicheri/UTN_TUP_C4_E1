Funcion Multiplicacion <- laremuneracion( n1,n2 )
	Definir Multiplicacion Como Real;
	Multiplicacion = n1 * n2;
Fin Funcion

Algoritmo Clase3
	Definir NOM Como Caracter
	Definir MES, AÑO Como Entero
	Definir HS, costo Como Real
	Escribir "Escriba su nombre y apellido: ";
	Leer NOM
	Escribir "Escriba el número del mes correspondiente al pago: ";
	Leer MES
	Escribir "Escriba el año correspondiente al pago: ";
	Leer AÑO
	Escribir "Escriba las horas totales que trabajó ese mes: ";
	Leer HS
	Escribir "Escriba costo por hora trabajada: ";
	Leer costo
	Escribir "Su remuneración del mes ", MES," del año ", AÑO 
	Escribir "es igual a $", laremuneracion(HS,costo)
	
FinAlgoritmo
	