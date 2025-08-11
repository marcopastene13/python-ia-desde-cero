def mostrar_info(nombre, edad, pais, nivel):
    print(f"Hola, {nombre} de {pais}.")
    print(f"Tienes {edad} años y tu nivel de python es {nivel}.")

    if nivel.lower() == "bajo":
        print("Sigue Practicando")
    elif nivel.lower() == "medio":
        print("sigue asi")
    elif nivel.lower() == "alto":
        print("excelente")
    else:
        print("no reconozco ese nivel")
        
mostrar_info("Marco", 28, "Chile", "medio")