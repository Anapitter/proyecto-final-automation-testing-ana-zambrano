import csv


def leer_datos_csv(ruta_archivo):
    """Lee un CSV con columnas 'usuario','password','expected_result' y devuelve
    una lista de tuplas (usuario, password, expected_result_bool).
    """
    datos = []
    with open(ruta_archivo, mode='r', encoding='utf-8', newline='') as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            # Normalizar campos y convertir expected_result a booleano
            usuario = (fila.get('usuario') or '').strip()
            password = (fila.get('password') or '').strip()
            expected_raw = (fila.get('expected_result') or '').strip().lower()
            expected = expected_raw in ('1', 'true', 'yes')
            datos.append((usuario, password, expected))
    return datos


if __name__ == '__main__':
    # Ejemplo de uso — apuntar a la nueva carpeta `datos`
    ruta = 'datos/data_login.csv'
    print(leer_datos_csv(ruta))