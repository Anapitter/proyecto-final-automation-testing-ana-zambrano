import json
from pathlib import Path

def leer_json_productos(ruta_archivo):
    ruta = Path(ruta_archivo)

    with ruta.open(encoding='utf-8') as archivo:
        productos = json.load(archivo)
        return productos  # devolvemos la lista completa, no solo los nombres
