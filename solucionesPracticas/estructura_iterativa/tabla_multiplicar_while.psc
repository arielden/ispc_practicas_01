Proceso TablaMultiplicarWhile
	
	Definir numero, multiplicador Como Entero
	
	Escribir "Ingrese un n�mero entre 1 y 10: "
	Leer numero
	
	multiplicador <- 1
	
	Mientras multiplicador <= 10 Hacer
		Escribir numero, " x ", multiplicador, " = ", numero * multiplicador
		multiplicador <- multiplicador + 1
	FinMientras
	
FinProceso