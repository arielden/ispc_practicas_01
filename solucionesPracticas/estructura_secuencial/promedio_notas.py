# Se piden las notas y se convierten a float
nota1 = float(input("Ingrese la nota de la primera materia: "))
nota2 = float(input("Ingrese la nota de la segunda materia: "))
nota3 = float(input("Ingrese la nota de la tercera materia: "))
nota4 = float(input("Ingrese la nota de la cuarta materia: "))
nota5 = float(input("Ingrese la nota de la quinta materia: "))

# se calcula la el promedio de las notas
suma = nota1 + nota2 + nota3 + nota4 + nota5
promedio = suma / 5

# Resultado
print(f"El promedio de las notas es: {promedio}")