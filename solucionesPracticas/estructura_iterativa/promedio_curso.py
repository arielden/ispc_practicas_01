cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes que rindieron el examen: "))

suma_notas = 0
for i in range(cantidad_estudiantes):
    nota = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
    suma_notas += nota

promedio = suma_notas / cantidad_estudiantes

if promedio > 8:
    print("El rendimiento del curso es elevado.")
elif promedio >= 6:
    print("El rendimiento del curso es aceptable.")
else:
    print("El rendimiento del curso es bajo.")
