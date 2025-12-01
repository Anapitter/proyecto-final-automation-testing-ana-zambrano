import json
import os

def leer_json_productos():
    """
    Lee los datos del archivo 'productos.json' ubicado en la carpeta 'data/' 
    relativa a la raíz del proyecto.
    """
    
    # 1. Obtener la ruta del directorio base del proyecto (un nivel más arriba de 'utils')
    # os.path.realpath(__file__) obtiene la ruta de este archivo (lector_json.py)
    # os.path.dirname(...) obtiene el directorio (utils)
    # os.path.dirname(...) obtiene el directorio padre (la raíz del proyecto)
    base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    
    # 2. Construir la ruta final: {raiz_del_proyecto}/data/productos.json
    json_file_path = os.path.join(base_dir, "data", "productos.json")
    
    # *** LÍNEA DE DIAGNÓSTICO (Opcional, pero útil para verificar) ***
    print(f"\n[DIAGNÓSTICO DESDE LECTOR] Buscando JSON en: {json_file_path}\n")

    # 3. Leer y retornar los nombres de los productos
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Validar la estructura y extraer solo los nombres para la parametrización
        if 'productos' in data and isinstance(data['productos'], list):
            nombres = [item['nombre'] for item in data['productos'] if 'nombre' in item]
            return nombres
        else:
            print("Error: El JSON no contiene la clave 'productos' o no es una lista válida.")
            return []
            
    except FileNotFoundError:
        print(f"Error CRÍTICO: El archivo de datos no se encontró en {json_file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {json_file_path} se encontró pero no es un JSON válido.")
        return []
    except Exception as e:
        print(f"Error inesperado al leer el JSON: {e}")
        return []