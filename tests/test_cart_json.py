from selenium import webdriver
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import pytest
from pathlib import Path
from utils.lector_json import leer_json_productos

RUTA_JSON = Path(__file__).resolve().parent.parent / "datos" / "productos.json"

from utils.lector_json import leer_json_productos

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
@pytest.mark.parametrize("nombre_producto_esperado", [leer_json_productos(RUTA_JSON)[0]["Nombre"]])

def test_car_json(login_in_driver, username, password, nombre_producto_esperado):
    """Verifica que se pueda agregar un producto al carrito y que aparezca en el carrito."""

    try:

        driver = login_in_driver(username, password,)
        inventory_page = InventoryPage(driver)

        # Agregar primer producto
        inventory_page.agregar_producto_por_nombre(nombre_producto_esperado)

        # Abrir carrito
        inventory_page.abrir_carrito()

        # Validar el producto en el carrito
        cart_page = CartPage(driver)

        assert cart_page.obtener_nombres_productos_carrito()[0] == nombre_producto_esperado, "El producto en el carrito no coincide con el esperado"
    
       
    except Exception as e:
        print(f"Error durante el test de inventario: {e}")
        raise

    finally:
        driver.quit()
