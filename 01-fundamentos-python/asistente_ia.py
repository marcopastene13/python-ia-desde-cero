print("Bienvenido a tu asistente de IA personal.")

nivel = input("¿Cual es tu nivel actual de Python? (bajo, medio, alto): ").lower()
if nivel == "bajo":
    print("Perfecto, comencemos con lo mas basico")
elif nivel == "medio":
    print("¡buen progreso! Vamos a repasar.")
elif nivel == "alto":
    print("¡Excelente! Estás listo para proyectos avanzados.")
else:
    print("no entendi tu respuesta, pero te ayudo igual.")

recomendacion = input("Quieres una recomendacion para hoy? (si / no): ").lower()

if recomendacion == "si":
    print("Te recomiendo que practiques con ejercicios de nivel " + nivel + ".")
else:
    print("¡Está bien! Si cambias de opinion, aquí estaré para ayudarte.")