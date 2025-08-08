print("agenda objetivos de estudio IA\n")

archivo = "objetivos.txt"

opcion = input("¿Quieres (1) agregar nuevos objetivos o (2) ver los objetivos guardados?:").strip()

if opcion == "1":
    with open(archivo, "a", encoding="utf-8") as f:
        while True:
            objetivo = input("Escribee un objetivo (o presiona Enter para terminar):").strip()
            if objetivo == "":
                break
            f.write(objetivo + "\n")
        print("objetivos guardados con exito")

elif opcion == "2":
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            objetivos = f.readlines()
            if objetivos:
                print("\n objetivos guardados:")
                for i, obj in enumerate(objetivos, 1):
                    print(f"{i}. {obj.strip()}")
            else:
                print("no hay objetivos gaurdados aun")
    except FileNotFoundError:
        print("No existe el archivo todavia. Agrega objetivos primero.")

else:
    print("opcion no valida.")
    