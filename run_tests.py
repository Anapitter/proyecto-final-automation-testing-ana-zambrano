"""
Script para ejecutar todas las pruebas del proyecto.
Genera reportes HTML y muestra resultados en la consola.
"""
import pytest
import os
from datetime import datetime

# Crear directorio de reportes si no existe
REPORTS_DIR = os.path.join(os.getcwd(), "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

# Generar nombre del reporte con timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_file = os.path.join(REPORTS_DIR, f"report_{timestamp}.html")

# Argumentos para ejecutar las pruebas
pytest_args = [
    "tests",
    "-v",
    f"--html={report_file}",
    "--self-contained-html",
    "-m", "not skip"
]

# Ejecutar pytest
if __name__ == "__main__":
    exit_code = pytest.main(pytest_args)
    print(f"\n✅ Reporte generado en: {report_file}")
    exit(exit_code)