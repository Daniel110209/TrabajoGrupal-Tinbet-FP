"""
main.py
Programa principal del Sistema Tinbet: menu, resumen y control general.
Registra usuarios (solo mayores de edad) y controla equipos y planes.
NO incluye el proceso de apuestas.
Responsable: Integrante 5

Ejecutar con:  python main.py
"""
from utilidades import leer_entero
from archivos import cargar_usuarios
from registro import registrar_usuario
from consultas import listar_usuarios, buscar_usuario
from equipos import gestionar_equipo, contar_disponibles


def mostrar_menu(titulo):
    print()
    print("==========================================")
    print("   " + titulo)
    print("==========================================")
    print(" 1. Registrar usuario")
    print(" 2. Listar usuarios registrados")
    print(" 3. Buscar usuario por DNI")
    print(" 4. Control de televisores (9)")
    print(" 5. Control de computadoras (10)")
    print(" 6. Control de camaras de seguridad (3)")
    print(" 7. Control de cables (3)")
    print(" 8. Control de planes de futbol (5)")
    print(" 9. Resumen general")
    print(" 0. Salir")
    print("==========================================")


def mostrar_resumen(datos, tv, pc, cam, cab, planes):
    print("\n--- RESUMEN GENERAL ---")
    print("Usuarios registrados (aceptados):", len(datos["dnis"]))
    print("Usuarios rechazados por ser menores:", datos["rechazados"])
    print("Televisores disponibles:       ", contar_disponibles(tv), "de", len(tv))
    print("Computadoras disponibles:      ", contar_disponibles(pc), "de", len(pc))
    print("Camaras disponibles:           ", contar_disponibles(cam), "de", len(cam))
    print("Cables disponibles:            ", contar_disponibles(cab), "de", len(cab))
    print("Planes de futbol disponibles:  ", contar_disponibles(planes), "de", len(planes))


def main():
    # Datos de usuarios (listas paralelas: la posicion i es el mismo usuario)
    datos = {
        "dnis": [],
        "nombres": [],
        "lugares": [],
        "edades": [],
        "codigos": [],
        "rechazados": 0,
    }
    cargar_usuarios(datos)

    # Estado de equipos: 0 = disponible, 1 = en uso / contratado
    tv = [0] * 9
    pc = [0] * 10
    cam = [0] * 3
    cab = [0] * 3
    planes = [0] * 5

    opcion = -1
    while opcion != 0:
        mostrar_menu("SISTEMA TINBET - ADMINISTRADOR")
        opcion = leer_entero("Elija una opcion: ")

        if opcion == 1:
            registrar_usuario(datos)
        elif opcion == 2:
            listar_usuarios(datos)
        elif opcion == 3:
            buscar_usuario(datos)
        elif opcion == 4:
            gestionar_equipo("Televisor", tv, "EN USO")
        elif opcion == 5:
            gestionar_equipo("Computadora", pc, "EN USO")
        elif opcion == 6:
            gestionar_equipo("Camara de seguridad", cam, "EN USO")
        elif opcion == 7:
            gestionar_equipo("Cable", cab, "EN USO")
        elif opcion == 8:
            gestionar_equipo("Plan de futbol", planes, "CONTRATADO")
        elif opcion == 9:
            mostrar_resumen(datos, tv, pc, cam, cab, planes)
        elif opcion == 0:
            print("\nCerrando el sistema. Hasta pronto.")
        else:
            print("\nOpcion no valida. Intente de nuevo.")


if __name__ == "__main__":
    main()
