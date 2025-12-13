from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import pytest

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_inventory(login_in_driver, username, password):
    """Verifica que se pueda agregar un producto al carrito y que aparezca en el carrito."""
    driver = login_in_driver(username, password)
    inventory_page = InventoryPage(driver)

    # Agregar primer producto
    inventory_page.agregar_primer_producto(0)

    # Abrir carrito
    inventory_page.abrir_carrito()

    # Validar el producto en el carrito
    cart_page = CartPage(driver)
    productos_carrito = cart_page.obtener_nombres_productos_carrito()
    assert len(productos_carrito) == 1, "El carrito no tiene el producto agregado"
