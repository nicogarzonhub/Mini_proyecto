import json
# Cargar datos desde JSON
def cargar_datos():
    try:
        with open("estudiantes.json", "r") as archivo:
            return json.load(archivo)
    except:
        return []
# Guardar datos en JSON
def guardar_datos():
    with open("estudiantes.json", "w") as archivo:
        json.dump(estudiantes, archivo)
# LISTA PRINCIPAL
estudiantes = cargar_datos()
# Calcular último ID
id_actual = max([e["id"] for e in estudiantes], default=0)
# Registrar estudiante
def registrar_estudiante():
    global id_actual  

    nombre = input("Escribe el nombre del estudiante: ")

    id_actual += 1
    estudiante = {"id": id_actual, "nombre": nombre}

    estudiantes.append(estudiante)
    guardar_datos()

    print(" Estudiante agregado!\n")
#mostrar lista de estidiantes
def mostrar_estudiante():
    if len(estudiantes) == 0:
        print("No hay estudiantes todavía\n")
    else:
        print("\n Lista de estudiantes:")
        for e in estudiantes:
            print(f'ID: {e["id"]} - Nombre: {e["nombre"]}')
        print()
# Eliminar estudiante por ID
def eliminar_estudiante():
    if len(estudiantes) == 0:
        print("No hay estudiantes para eliminar\n")
        return
    try:
        id_buscar = int(input("Ingresa el ID del estudiante a eliminar: "))
    except:
        print("ID inválido\n")
        return
    for e in estudiantes:
        if e["id"] == id_buscar:
            estudiantes.remove(e)
            guardar_datos()
            print(" Estudiante eliminado!\n")
            return
    print("No existe un estudiante con ese ID.\n")
# Actualizar estudiante por ID
def actualizar_estudiante():
    if len(estudiantes) == 0:
        print("No hay estudiantes para actualizar\n")
        return
    try:
        id_buscar = int(input("Ingresa el ID del estudiante a actualizar: "))
    except:
        print("ID inválido\n")
        return
    for e in estudiantes:
        if e["id"] == id_buscar:
            nuevo = input("Nuevo nombre: ")
            e["nombre"] = nuevo
            guardar_datos()
            print(" Estudiante actualizado!\n")
            return
    print(" No existe un estudiante con ese ID.\n")
# MENÚ
while True:
    print("= MENÚ PRINCIPAL =")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Eliminar estudiante")
    print("4. Actualizar estudiante")
    print("5. Salir")
    opcion = input("Elige una opción (1-4): ")
    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        mostrar_estudiante()
    elif opcion == "3":
        eliminar_estudiante()
    elif opcion == "4":
        actualizar_estudiante()
    elif opcion == "5":
        print("Gracias por usar el programa.")
        break
    else:
        print("Opción inválida\n")
