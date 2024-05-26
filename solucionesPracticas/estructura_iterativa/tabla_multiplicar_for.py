numero = int(input("Ingrese un número entre 1 y 10: "))

for multiplicador in range(1, 11):  # 11 para incluir el 10
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
