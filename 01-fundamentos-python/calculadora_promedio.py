print("calculadora de promedio de notas de Python.")

notas = []

for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"ingrese la nota {i} (0.0 a 7.0): ").strip())
            if 0.0 <= nota <= 7.0:
                notas.append(nota)
                break
            else:
                print(" la nota debe estar entre 0.0 y 7.0")
        except ValueError:
            print(" Por favor ingrese un numero valido.")

promedio = sum(notas) / len(notas)

print(f"\n tus notas fueron: {notas}")
print(f" tu primedio es: {promedio:.2f}")

if promedio >= 6.0:
    print("excelente, sigue asi!!")
elif promedio >= 4.0:
    print("bien, pero puedes mejorar.")
else:
    ("necesitas reforzar tus practicas.")