# Sistema Tinbet - Registro de usuarios y control de equipos

Prototipo en Python del informe de bitácora de Tinbet (KING TECH CORPORATION).

El sistema:
- Registra usuarios (DNI, nombre completo, lugar donde vive y edad).
- Rechaza a los menores de 18 años.
- Genera un código único de 12 números por usuario.
- Guarda los usuarios en el archivo `usuarios.txt`.
- Controla 9 televisores, 10 computadoras, 3 cámaras, 3 cables y 5 planes de fútbol (disponible / en uso).

> No incluye el proceso de apuestas.

## Cómo ejecutarlo

```
python main.py
```

## Estructura y responsables

| Archivo | Qué hace | Responsable |
|---|---|---|
| `utilidades.py` | Formatear DNI, generar código de 12 números, buscar en listas, leer enteros | Jheimy |
| `archivos.py` | Guardar y cargar usuarios en `usuarios.txt` | Jheimy |
| `registro.py` | Registrar usuario y validar edad | Diego |
| `consultas.py` | Mostrar, listar y buscar usuarios por DNI | Oscar |
| `equipos.py` | Control de equipos y planes | Erick |
| `main.py` | Menú principal y resumen general | Misael |

## Integrantes

- Jheimy (creó el repositorio)
- Diego
- Oscar
- Erick
- Misael
