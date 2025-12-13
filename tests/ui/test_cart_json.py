"""
Tests del carrito usando datos desde el archivo JSON.
Valida que se puedan agregar productos del JSON al carrito.
"""
import pytest
from utils.lector_json import leer_json_productos
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


# ===============================
# FIXTURE PARA CARGAR PRODUCTOS
# ===============================
@pytest.fixture(scope="module")
def productos_json():
    """Carga los productos desde el archivo JSON."""
    try:
        datos = leer_json_productos()
        if not datos or len(datos) == 0:
            pytest.skip("El JSON de productos está vacío")
        return datos
    except FileNotFoundError:
        pytest.skip("No se encontró el archivo de productos")
    except Exception as e:
        pytest.skip(f"Error al leer el JSON: {e}")


# ===============================
# TESTS
# ===============================
@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_agregar_producto_por_nombre_json(login_in_driver, username, password, productos_json):
    """
    Prueba agregar el primer producto del JSON al carrito.
    """
    driver = login_in_driver(username, password)
    
    inventory_page = InventoryPage(driver)

    # Obtener el primer producto del JSON
    primer_producto = productos_json[0]

    # Agregar el producto al carrito por su nombre
    inventory_page.agregar_producto_por_nombre(primer_producto)

    # Verificar que se agregó
    conteo = inventory_page.obtener_conteo_carrito()
    assert conteo == 1, f"Se esperaba 1 producto, pero se encontraron {conteo}"

    # Abrir carrito y validar
    inventory_page.abrir_carrito()
    cart_page = CartPage(driver)
    productos_en_carrito = cart_page.obtener_nombres_productos_carrito()

    assert primer_producto in productos_en_carrito, f"El producto '{primer_producto}' no está en el carrito"


@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_agregar_multiples_productos_json(login_in_driver, username, password, productos_json):
    """
    Prueba agregar múltiples productos del JSON al carrito.
    """
    driver = login_in_driver(username, password)
    
    inventory_page = InventoryPage(driver)

    # Agregar los primeros dos productos del JSON
    productos_a_agregar = productos_json[:2]

    for producto in productos_a_agregar:
        inventory_page.agregar_producto_por_nombre(producto)

    # Verificar que se agregaron ambos
    conteo = inventory_page.obtener_conteo_carrito()
    assert conteo == len(productos_a_agregar), f"Se esperaban {len(productos_a_agregar)} productos, pero se encontraron {conteo}"

    # Abrir carrito y validar
    inventory_page.abrir_carrito()
    cart_page = CartPage(driver)
    productos_en_carrito = cart_page.obtener_nombres_productos_carrito()

    for producto in productos_a_agregar:
        assert producto in productos_en_carrito, f"El producto '{producto}' no está en el carrito"
