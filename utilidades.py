"""
utilidades.py
Funciones de apoyo usadas por todo el sistema Tinbet.
Responsable: Integrante 1
"""
import random


def formatear_dni(numero):
    """Convierte el DNI a texto de 8 digitos (rellena con ceros a la izquierda)."""
    texto = str(numero)
    while len(texto) < 8:
        texto = "0" + texto
    return texto


def generar_codigo(largo):
    """Genera un codigo de 'largo' numeros (se usa con 12)."""
    codigo = ""
    for _ in range(largo):
        codigo = codigo + str(random.randint(0, 9))
    return codigo


def existe_texto(lista, valor):
    """Devuelve True si 'valor' ya esta dentro de la lista."""
    for elemento in lista:
        if elemento == valor:
            return True
    return False


def leer_entero(mensaje):
    """Pide un numero entero y repite la pregunta hasta que se escriba uno valido."""
    while True:
        texto = input(mensaje).strip()
        if texto.lstrip("-").isdigit():
            return int(texto)
        print("Entrada no valida. Escriba solo numeros.")
