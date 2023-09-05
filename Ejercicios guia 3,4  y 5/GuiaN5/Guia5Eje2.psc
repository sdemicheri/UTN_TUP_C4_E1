Algoritmo raices
	A <- real
	B <- real
	C <- real
	Escribir "Ingrese A, B y C"
	Leer A , B , C
	si (B^2-4*A*C) >= 0;	
		Entonces
		x1 <- (-B+((B^2-4*A*C)^(1/2)))/2*A
		x2 <- (-B-((B^2-4*A*C)^(1/2)))/2*A
		Escribir "Las Raices son: " , x1 , " " , x2
	SiNo
		Escribir "Las raices obtenidas no estan dentro de los numeros Reales"
	FinSi
FinAlgoritmo
