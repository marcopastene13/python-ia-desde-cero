def tabla_multiplicar(n):
    print(f"\ tabla de multiplicar del {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

while True:
    print("\n--- MENU TABLAS DE MULTIPLICAR ---")
    print("1. Ver una tabla de multiplicar")
    print("2. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        try:
            numero = int(input("Escribe un numero para ver su tabla de multiplicar: "))
            tabla_multiplicar(numero)
        except ValueError:
            print(" debes escribir un numero valido.")
    elif opcion == "2":
        print("saliendo del programa...")
        break
    else:
        print("opcion invalida, intanta denuevo")
        
