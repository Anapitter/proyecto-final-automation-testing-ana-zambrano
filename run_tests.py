import pytest
import os
from datetime import datetime

# Lista de archivos a ejecutar

test_files = [
    "tests/test_login.py",
    "tests/test_inventory.py",
    "tests/test_cart.py",
    "tests/test_cart_json.py"
]

# Argumentos para ejecutar las pruebas
pytest_args = ["--html = report.html", "--self-contained-html", "--v"]
    
pytest.main(pytest_args)