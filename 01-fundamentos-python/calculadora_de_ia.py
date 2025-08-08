def plan_estudio():
    print("Bienvenido a la calculadora de tiempo de estudio de IA")

    nivel = input("¿cual es tu niveld e Python? (bajo / medio / alto): ").strip().lower()

    try:
        minutos = int(input("¿cuantos minutos tienes hoy para estudiar?: ").strip())
    except ValueError:
        print("ingres numero valido para minutos.")
        return
    print("\n Analizando tu plan de estudio...\n")

    if nivel == "bajo":
        if minutos < 20:
            print("revisa variables y tipos de datos.")
        elif minutos <= 40:
            print("Practica condicionales y bucles simples.")
        else:
            print("haz ejercicios con listas y funciones.")

    elif nivel == "medio":
        if minutos < 20:
            print("lee teoria sibre estructura de datos.")
        elif minutos <= 40:
            print("haz ejercicios combinados de logica y funciones.")
        else:
            print("empieza un mini proyecto (calculadora, sistema de tareas, etc.).")
    
    if nivel == "alto":
        if minutos < 20:
            print("repasa teoria de algoritmos")
        elif minutos <= 40:
            print("trabaja con pandas o numpy.")
        else:
            print("crea un modelo basico de machine learning.")

    else:
        print("nivel no reconocido. prueba con bajo, medio o alto.")


plan_estudio()