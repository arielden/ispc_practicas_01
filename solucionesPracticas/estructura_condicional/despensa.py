cantidad = int(input("Ingrese la cantidad de leche (en litros): "))
es_jubilado = input("¿Es jubilado? (Si/No): ").lower()

precio_unitario = 1000
descuento = 0

if cantidad > 12:
    if cantidad > 24:
        descuento = 0.15
    else:
        descuento = 0.10

if es_jubilado:
    descuento += 0.10

precio_final = cantidad * precio_unitario * (1 - descuento)

print("El precio final es: $", precio_final)