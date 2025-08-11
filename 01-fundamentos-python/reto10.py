inventario = {}

def mostrar_inventario():
    if not inventario:
        print("El inventario esta vacio.")
    else:
        for producto, datos in  inventario.items():
            print(f"{producto} - Precio: ${datos['precio']} - Stock: {datos['stock']} - Peso: {datos['peso']}")

def agregar_producto():
    nombre = input("nombre del producto: ").lower()
    precio = int(input("Precio del producto: "))
    stock = int(input("cantidad inicial: "))
    peso = int(input("Peso del producto: "))
    inventario[nombre] = {"precio": precio, "stock": stock, "peso": peso}
    print(f"{nombre} agregado al inventario.")


def eliminar_producto():
    nombre = input("Producto a elminar: ").lower()
    if nombre in inventario:
        del inventario[nombre]
        print(f"{nombre} eliminado.")
    else:
        print("ese producto no existe.")

def actualizar_stock():
    nombre = input("Producto a actualizar: ").lower()
    if nombre in inventario:
        cantidad = int(input("Cantidad a agregar/restar (puede ser negativa): "))
        inventario[nombre]["stock"] += cantidad
        print(f"Stock de {nombre} actualizado.")
    else:
        print("Ese producto no existe.")       

def vender_producto():
    nombre = input("Producto a vender: ").lower()
    if nombre in inventario:
        cantidad = int(input("cantidad a vender: "))
        if cantidad <= inventario[nombre]["stock"]:
            total = cantidad * inventario[nombre]["precio"]
            inventario[nombre]["stock"] -= cantidad
            print(f"Venta realizada. Total: ${total}")
        else:
            print("No hay suficiente stock.")
    else:
        print("ese producto no existe.")


while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Actualizar stock")
    print("5. Vender producto")
    print("6. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        eliminar_producto()
    elif opcion == "4":
        actualizar_stock()
    elif opcion == "5":
        vender_producto()
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opcion invalida.")

