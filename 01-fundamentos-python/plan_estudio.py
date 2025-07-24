tareas = [
    "Repasar variables y tipos de datos",
    "hacer 3 ejercicios de condicionales",
    "ver un video de listas en youtube",
    "Practicar bucles con ejercicio real",
    "Leer documentacion de Python"
]

for tarea in tareas:
    print(f"\n➡️ Tarea: {tarea}")
    completada = input("¿Has completado esta tarea? (si/no): ").strip().lower()

    if completada == "si":
        print("¡Excelente trabajo! Sigue así.")

    else:
        print("No te preocupes, puedes intentarlo más tarde.")

print("\n ¿cuantas tareas hiciste hoy?")
realizadas = int(input("Numero: "))

if realizadas >= 3:
    print("¡Buen trabajo!!")
else:
    print("No te preocupes, puedes mejorar mañana.")

print("n📋 Has revisado tu plan de estudio completo por hoy.")