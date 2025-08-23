usuarios = [
    {"id": 1, "nombre": "Marco", "pais": "Chile"},
    {"id": 2, "nombre": "Javiera", "pais": "Brasil"},
]

def listar_usuarios():
    return usuarios 

def buscar_usuarios(id):
    for u in usuarios:
        if u["id"] == id:
            return u
    return {"error": "Usuario no encontrado"}

def agregar_usuario(nombre, pais):
    nuevo_id = len(usuarios) + 1
    usuarios.append({"id": nuevo_id, "nombre": nombre, "pais": pais})
    return {"mensaje": "usuario agregado", "usuario": usuarios[-1]}


print("listar usuarios:", listar_usuarios())
print("buscar usuario con id=1:", buscar_usuarios(1))
print("agregar nuevo usuario:", agregar_usuario("Leo", "Chile"))
print("listar usuarios actualizados:", listar_usuarios())