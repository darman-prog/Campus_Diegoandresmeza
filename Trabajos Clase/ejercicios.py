lista_de_tareas = []

def agregar_tarea(tarea, prioridad):
    tarea_nueva = {"nombre": tarea, "prioridad": prioridad}
    lista_de_tareas.append(tarea_nueva)
    print("Tarea agregada con éxito.")

def mostrar_tareas():
    if not lista_de_tareas:
        print("No hay tareas pendientes.")
        return

    tareas_ordenadas = sorted(lista_de_tareas, key=lambda x: x["prioridad"], reverse=True)

    print("Tareas pendientes:")
    for idx, tarea in enumerate(tareas_ordenadas, start=1):
        print(f"{idx}. {tarea['nombre']} - Prioridad: {tarea['prioridad']}")

def eliminar_tarea():
    if not lista_de_tareas:
        print("No hay tareas pendientes para eliminar.")
        return

    tarea_a_eliminar = input("Ingrese el nombre de la tarea que desea eliminar: ")
    tarea_encontrada = False

    for tarea in lista_de_tareas:
        if tarea["nombre"] == tarea_a_eliminar:
            lista_de_tareas.remove(tarea)
            tarea_encontrada = True
            print("Tarea eliminada con éxito.")
            break

    if not tarea_encontrada:
        print("Error: La tarea ingresada no existe.")

while True:
    print("\nMenú:")
    print("1. Añadir una nueva tarea.")
    print("2. Mostrar todas las tareas pendientes.")
    print("3. Eliminar una tarea.")
    print("4. Salir del programa.")

    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == "1":
        nueva_tarea = input("Ingrese el nombre de la nueva tarea: ")
        prioridad = int(input("Ingrese la prioridad de la tarea (1-5): "))
        agregar_tarea(nueva_tarea, prioridad)
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
