'''
Desarrollar en Python un módulo que gestione una agenda telefónica en un diccionario de Python
utilizando los recursos ya vistos (variables, input, print, if, if - else, while, for)
que consideren adecuados para cada uno de estos casos:

Mostrar al usuario un menú de opciones

Opción 1: Agregar una persona (apellido, nombre, dni, email y número de teléfono).
    Esta opción debe agregar al diccionario a la persona que el usuario ingrese
Opción 2: Modificar una persona: dado su dni debe buscar la persona y preguntar si
    desea cambiar los demás campos de la persona, cambiando los que quiera.
Opción 3: Eliminar una persona del diccionario. Elimina según el DNI
Opción 4: Mostrar todos la agenda
Opción 5: Salir
'''

agenda = {}

while True:
    print("\n--- Menú ---")
    print("1. Agregar persona")
    print("2. Modificar persona")
    print("3. Eliminar persona")
    print("4. Mostrar agenda")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        dni = input("DNI: ")
        if dni in agenda:
            print("El DNI ya existe.")
        else:
            agenda[dni] = {
                'apellido': input("Apellido: "),
                'nombre': input("Nombre: "),
                'email': input("Email: "),
                'telefono': input("Teléfono: ")
            }
            print("Persona agregada.")

    elif opcion == '2':
        dni = input("DNI de la persona a modificar: ")
        if dni in agenda:
            print("Datos actuales:", agenda[dni])
            for campo in agenda[dni]:
                nuevo_valor = input(f"Nuevo valor para {campo} (dejar en blanco para no modificar): ")
                if nuevo_valor:
                    agenda[dni][campo] = nuevo_valor
            print("Persona modificada")
        else:
            print("DNI no encontrado")

    elif opcion == '3':
        dni = input("DNI de la persona a eliminar: ")
        if dni in agenda:
            del agenda[dni]
            print("Se eliminó a la persona")
        else:
            print("No se encuentra DNI")

    elif opcion == '4':
        if agenda:
            for dni, datos in agenda.items():
                print(f"\nDNI: {dni}")
                for campo, valor in datos.items():
                    print(f"{campo}: {valor}")
        else:
            print("Agenda vacía")

    elif opcion == '5':
        print("Saliendo...")
        break
    else:
        print("Opción inválida")
