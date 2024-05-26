Proceso TrabajoPintura
	
	Definir ancho, alto, costo_por_metro, area, costo_total Como Real;
	
	Escribir "Ingresar ancho de la pared (m): ";
	Leer ancho;
	
	Escribir "Ingresar alto de la pared (m): ";
	Leer alto;
	
	Escribir "Ingrese el costo de mano de obra por (m2): ";
	Leer costo_por_metro;
	
	area <- ancho * alto;
	costo_total <- area * costo_por_metro;
	
	Escribir "El costo total del trabajo es: $", costo_total;
	
FinProceso
