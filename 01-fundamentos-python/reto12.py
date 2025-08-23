tareas = []

def mostrar_tareas():
    if not tareas:
        print("no tienes tareas.")
    else:
        print("\n tus tareas:")
        for i, tarea in enumerate(tareas, 1):
            estado = "check" if tarea["completada"] else "X"
            print(f"{i}. {tarea['nombre']} - {estado}")

def agregar_tarea():
    nombre = input ("escribe la nueva tarea: ")
    tareas.append({"nombre": nombre, "completada": False})
    print(f"Tarea '{nombre}' agregada.")

def completar_tarea():
    mostrar_tareas()
    try:
        num = int(input("numero de la tarea a completar: "))
        tareas[num-1]["completada"] = True
        print("tarea marcada como completada.")
    except (IndexError, ValueError):
        print("numero invalido")

def eliminar_tarea():
    mostrar_tareas()
    try:
        num = int(input("Número de la tarea a eliminar: "))
        eliminada = tareas.pop(num-1)
        print(f"Tarea '{eliminada['nombre']}' eliminada.")
    except (IndexError, ValueError):
        print("Número inválido.")

# Menu Principal 
while True:
    print("\n--- MENU ---")
    print("1. Mostrar Tareas")
    print("2. Agregar Tareas")
    print("3. Completar Tareas")
    print("4. Eliminar Tarea")
    print("5. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("Saliendo de tu lista de tareas...")
        break
    else:
        print("Opción inválida.")