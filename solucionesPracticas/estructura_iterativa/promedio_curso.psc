Proceso PromedioCurso
	
	Definir cantidad_estudiantes, i Como Entero
	Definir nota, suma_notas, promedio Como Real
	
	Escribir "Ingrese la cantidad de estudiantes que rindieron el examen: "
	Leer cantidad_estudiantes
	
	suma_notas <- 0
	
	Para i <- 1 Hasta cantidad_estudiantes Con Paso 1 Hacer
		Escribir "Ingrese la nota del estudiante ", i, ": "
		Leer nota
		suma_notas <- suma_notas + nota
	FinPara
	
	promedio <- suma_notas / cantidad_estudiantes
	
	Si promedio > 8 Entonces
		Escribir "El rendimiento del curso es elevado."
	Sino
		Si promedio >= 6 Entonces
			Escribir "El rendimiento del curso es aceptable."
		Sino
			Escribir "El rendimiento del curso es bajo."
		FinSi
	FinSi
	
FinProceso