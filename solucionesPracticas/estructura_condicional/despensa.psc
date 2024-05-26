Proceso Despensa
	
	Definir cantidad, precio_unitario, descuento, precio_final Como Real
	Definir es_jubilado Como Logico
	Definir respuesta Como Caracter
	
	Escribir "Ingrese la cantidad de leche (en litros): "
	Leer cantidad
	Escribir "¿Es jubilado? (Si/No): "
	Leer respuesta
	
	Si respuesta = "Si" Entonces
		es_jubilado <- Verdadero
	Sino
		es_jubilado <- Falso
	FinSi
	
	precio_unitario <- 1000
	descuento <- 0
	
	Si cantidad > 12 Entonces
		Si cantidad > 24 Entonces
			descuento <- 0.15
		Sino
			descuento <- 0.10
		FinSi
	FinSi
	
	Si es_jubilado Entonces
		Si descuento > 0 Entonces
			descuento <- descuento + 0.10
		Sino
			descuento <- 0.10
		FinSi
	FinSi
	
	precio_final <- cantidad * precio_unitario * (1 - descuento)
	
	Escribir "El precio final es: $", precio_final
	
FinProceso