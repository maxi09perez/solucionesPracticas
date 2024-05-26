agenda = {}
op = 0
while op != 5:
    print("***Menu de la Agenda***")
    print("1. Agregar contacto.")
    print("2. Modificar contacto.")
    print("3. Eliminar contacto.")
    print("4. Mostrar todos los contactos agendados.")
    print("5. Salir")
    
    op=int(input("Seleccione ua opcion: "))

    if op == 1:
        apellido = input("Ingrese apellido: ")
        nombre = input("Ingrese nombre: ")
        dni = input("Ingrese DNI: ")
        email= input("Ingrese Email: ")
        telefono = input("Ingrese numero de telefono: ")
        agenda[dni]= {"Apellido": apellido, "Nombre": nombre, "DNI": dni, "Email": email, "Telefono": telefono}
    elif op == 2:
        dni = input("Ingrese el dni del contacto a modificar: ")
        if dni in agenda:
            dato = input("Que dato desea modificar? (apellido/nombre/email/telefono): ")
            if dato in agenda[dni]:
                nv = input(f"Ingrese el nuevo valor para {dato}: ")
                agenda[dni][dato] = nv
            else:
                print("Campo no valido!")
        else:
            print("No existe Contacto registrado con ese DNI!")
    elif op == 3:
        dni = input("Ingrese DNI del contacto a eliminar: ")
        if dni in agenda:
            del agenda[dni]
        else:
            print("No existe Contacto registrado con ese DNI!")
    elif op == 4:
        for dni, datos in agenda.items():
            print(f"Apellido: {datos['Apellido']}")
            print(f"Nombre: {datos['Nombre']}")
            print(f"DNI: {datos['DNI']}")
            print(f"Email: {datos['Email']}")
            print(f"Teléfono: {datos['Telefono']}")
            print("-" * 30)
    elif op == 5:
        print("Gracias por usar el programa Agenda!")
    else:
        print("Opcion incorrecta! Vuelva a intentarlo")