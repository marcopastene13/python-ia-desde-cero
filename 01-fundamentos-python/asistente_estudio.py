print("Bienvenido a tu mini Asistente IA")

nivel = input("¿cual es tu nivel de Python? (bajo / medio / alto): ").strip().lower()

try: 
    tiempo = int(input("¿cuantos minutos tienes disponibles hoy?: ").strip())
except ValueError:
    print("Por favor, escribe un numero valido.")
    exit()

print("\n analizando tu perfil...\n")

if nivel == "bajo":
    if tiempo < 25:
        print("revisa variables y tipos de datos.")
    elif tiempo <= 50:
        print("practica condicionales con ejemplos.")
    else:
        print("haz ejercicios de listas, funciones y bucles")

elif nivel == "medio":
    if tiempo < 20:
        print("📌 Lee teoría sobre estructuras de datos.")
    elif tiempo <= 40:
        print("📌 Haz ejercicios combinados de lógica.")
    else:
        print("📌 Empieza un mini proyecto, como una calculadora o un sistema de tareas.")
elif nivel == "alto":
    if tiempo < 20:
        print("📌 Repasa teoría de algoritmos y estructuras.")
    elif tiempo <= 40:
        print("📌 Revisa librerías como `pandas` o `numpy`.")
    else:
        print("📌 Intenta hacer un modelo básico de machine learning con `scikit-learn`.")
else:
    print("⚠️ No reconocí tu nivel, pero te recomiendo repasar ejercicios anteriores.")
