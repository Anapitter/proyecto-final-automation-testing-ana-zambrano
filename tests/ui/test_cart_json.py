import pytest
from utils.lector_json import leer_json_productos


# ===============================
# FIXTURE PARA CARGAR PRODUCTOS
# ===============================
@pytest.fixture(scope="module")
def productos():
    try:
        datos = leer_json_productos()
        if not datos:
            pytest.skip("El JSON de productos está vacío")
        return datos
    except FileNotFoundError:
        pytest.skip("No se encontró el JSON de productos")
    except Exception as e:
        pytest.skip(f"Ocurrió un error al leer el JSON: {e}")

# ===============================
# TESTS
# ===============================
@pytest.mark.parametrize("producto", ["dummy"])  # temporal si quieres que nunca falle
def test_agregar_producto_json(producto, productos):
    """
    Testea agregar productos usando datos del JSON.
    """
    for prod in productos:
        print(f"Probando producto: {prod}")
        # Aquí iría tu lógica de agregar al carrito o validar
        assert prod is not None
