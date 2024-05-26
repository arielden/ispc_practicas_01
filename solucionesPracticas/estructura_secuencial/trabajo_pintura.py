# Leer los datos de entrada
ancho = float(input("Ingresar ancho de la pared (m): "))
alto = float(input("Ingresar alto de la pared (m): "))
costo_por_metro = float(input("Ingrese el costo de mano de obra por (m2): "))

# Calcular el área y el costo total
area = ancho * alto
costo_total = area * costo_por_metro

# Mostrar el resultado
print("El costo total del trabajo es: $", costo_total)