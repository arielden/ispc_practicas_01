partidos = []
semanas = 0
partidos_campeonato = 5
while semanas < partidos_campeonato:
    resultado = input("El resultado de la semana es (G, E, P): ").upper()
    partidos.append(resultado)
    puntos = 0
    for partido in partidos:
        if partido == "G":
            puntos += 3
        elif partido == "E":
            puntos += 1
    print(f"Se llevan jugados {len(partidos)} partidos, con un total de {puntos} puntos")
    semanas += 1
print(f"Fin del campeonato!!, se jugaron {len(partidos)} partidos, total del equipo {puntos} puntos")