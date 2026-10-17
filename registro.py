"""
registro.py
Registro de usuarios: valida DNI y edad, rechaza menores de edad,
genera el codigo de 12 numeros y guarda al usuario.
Responsable: Integrante 2
"""
from utilidades import formatear_dni, generar_codigo, existe_texto, leer_entero
from archivos import guardar_usuarios
from consultas import mostrar_usuario

EDAD_MINIMA = 18


def registrar_usuario(datos):
    print("\n--- REGISTRO DE USUARIO ---")

    # 1. DNI
    dni_num = leer_entero("Ingrese el DNI (8 digitos): ")
    if dni_num < 1 or dni_num > 99999999:
        print("DNI no valido. Debe tener 8 digitos.")
        return
    dni = formatear_dni(dni_num)
    if existe_texto(datos["dnis"], dni):
        print("Ese DNI ya esta registrado.")
        return

    # 2. Edad (se verifica antes de pedir mas datos)
    edad = leer_entero("Ingrese la edad: ")
    if edad < 0 or edad > 120:
        print("Edad no valida.")
        return
    if edad < EDAD_MINIMA:
        datos["rechazados"] = datos["rechazados"] + 1
        print("\nREGISTRO RECHAZADO: el usuario es menor de edad.")
        print("No cumple con el requisito de edad minima (18 anios).")
        return

    # 3. Datos restantes
    nombre = input("Ingrese el nombre completo: ").strip()
    lugar = input("Ingrese el lugar donde vive: ").strip()
    if len(nombre) == 0 or len(lugar) == 0:
        print("Datos incompletos. No se registro al usuario.")
        return

    # 4. Codigo unico de 12 numeros
    codigo = generar_codigo(12)
    while existe_texto(datos["codigos"], codigo):
        codigo = generar_codigo(12)

    # 5. Guardar
    datos["dnis"].append(dni)
    datos["nombres"].append(nombre)
    datos["lugares"].append(lugar)
    datos["edades"].append(edad)
    datos["codigos"].append(codigo)
    guardar_usuarios(datos)

    print("\nUSUARIO ACEPTADO Y REGISTRADO")
    mostrar_usuario(datos, len(datos["dnis"]) - 1)
