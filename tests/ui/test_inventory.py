from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest


from pages.inventory_page import InventoryPage

# PARAMETRIZACIÓN QUE QUIERE TU PROFESOR
@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce")
])
def test_inventory(login_in_driver, username, password):
    driver = None
    try:
        # login parametrizado
        driver = login_in_driver(username, password)
        inventory_page = InventoryPage(driver)

        # 1. Verificar que hay productos
        assert len(inventory_page.obtener_todos_los_productos()) > 0, "No hay productos en el inventario"

        # 2. Verificar carrito vacío al inicio
        assert inventory_page.obtener_conteo_carrito() == 0, "El carrito no está vacío al inicio"

        # 3. Agregar un producto
        inventory_page.agregar_primer_producto()
        assert inventory_page.obtener_conteo_carrito() == 1, "El carrito no tiene 1 producto después de agregar"

    finally:
        if driver:
            driver.quit()
