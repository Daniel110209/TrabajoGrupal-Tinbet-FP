"""
equipos.py
Control de equipos y planes: televisores, computadoras, camaras,
cables y planes de futbol. Cada uno esta DISPONIBLE (0) o EN USO (1).
Responsable: Integrante 4
"""
from utilidades import leer_entero


def gestionar_equipo(nombre, estado, texto_ocupado):
    """Muestra el estado de cada equipo y permite cambiarlo.
    'estado' es una lista de 0 (disponible) y 1 (en uso/contratado)."""
    cantidad = len(estado)
    while True:
        print("\n--- CONTROL:", nombre, "---")
        for i in range(cantidad):
            if estado[i] == 0:
                print(f"{i + 1}. {nombre} {i + 1}: DISPONIBLE")
            else:
                print(f"{i + 1}. {nombre} {i + 1}: {texto_ocupado}")
        num = leer_entero("Ingrese el numero para cambiar su estado (0 = volver al menu): ")
        if num == 0:
            return
        if 1 <= num <= cantidad:
            estado[num - 1] = 1 - estado[num - 1]
            print("Estado actualizado.")
        else:
            print("Numero fuera de rango.")


def contar_disponibles(estado):
    """Cuenta cuantos elementos estan disponibles (valor 0)."""
    disponibles = 0
    for valor in estado:
        if valor == 0:
            disponibles = disponibles + 1
    return disponibles
