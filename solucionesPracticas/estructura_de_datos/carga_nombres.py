# Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 

nombres = []
while len(nombres) < 10:
    nombre = input("Ingrese un nombre: ")
    if nombre not in nombres:
        nombres.append(nombre)
    else:
        print("Nombre repetido. Intente otra vez")

print("Nombres ingresados:", nombres)

# Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo

del nombres[2]
del nombres[-1]
nombres.sort()
print("Lista ordenada:", nombres)
