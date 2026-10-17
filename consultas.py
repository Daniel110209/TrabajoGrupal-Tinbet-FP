"""
consultas.py
Consultas de usuarios: mostrar uno, listar todos y buscar por DNI.
Responsable: Integrante 3
"""
from utilidades import formatear_dni, leer_entero


def mostrar_usuario(datos, pos):
    """Muestra los datos del usuario que esta en la posicion 'pos'."""
    print("DNI:               ", datos["dnis"][pos])
    print("Nombre completo:   ", datos["nombres"][pos])
    print("Lugar de vivienda: ", datos["lugares"][pos])
    print("Edad:              ", datos["edades"][pos])
    print("Codigo (12 num):   ", datos["codigos"][pos])


def listar_usuarios(datos):
    print("\n--- USUARIOS REGISTRADOS ---")
    total = len(datos["dnis"])
    if total == 0:
        print("Aun no hay usuarios registrados.")
        return
    for i in range(total):
        print("Usuario", i + 1, ":")
        mostrar_usuario(datos, i)
        print("------------------------------")


def buscar_usuario(datos):
    print("\n--- BUSCAR USUARIO ---")
    dni_num = leer_entero("Ingrese el DNI a buscar: ")
    dni = formatear_dni(dni_num)
    encontrado = False
    for i in range(len(datos["dnis"])):
        if datos["dnis"][i] == dni:
            print("Usuario encontrado:")
            mostrar_usuario(datos, i)
            encontrado = True
    if not encontrado:
        print("No existe un usuario con ese DNI.")
