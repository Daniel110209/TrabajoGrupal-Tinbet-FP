"""
archivos.py
Guarda y carga los usuarios en un archivo de texto (usuarios.txt)
para que los datos no se pierdan al cerrar el programa.
Responsable: Integrante 1
"""
import os

ARCHIVO = "usuarios.txt"


def guardar_usuarios(datos):
    """Escribe todos los usuarios en el archivo, uno por linea."""
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for i in range(len(datos["dnis"])):
            linea = "|".join([
                datos["dnis"][i],
                datos["nombres"][i],
                datos["lugares"][i],
                str(datos["edades"][i]),
                datos["codigos"][i],
            ])
            archivo.write(linea + "\n")


def cargar_usuarios(datos):
    """Lee el archivo (si existe) y llena las listas de datos."""
    if not os.path.exists(ARCHIVO):
        return
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split("|")
            if len(partes) == 5:
                datos["dnis"].append(partes[0])
                datos["nombres"].append(partes[1])
                datos["lugares"].append(partes[2])
                datos["edades"].append(int(partes[3]))
                datos["codigos"].append(partes[4])
