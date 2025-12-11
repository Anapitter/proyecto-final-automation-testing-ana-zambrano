"""
Tests de la página de Inventario de Sauce Demo.
Valida la funcionalidad de agregar productos al carrito.
"""
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import pytest


@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_inventory_productos_disponibles(login_in_driver, username, password):
    """Verifica que hay productos disponibles en el inventario."""
    driver = login_in_driver(username, password)

    try:
        inventory_page = InventoryPage(driver)
        
        # Verificar que hay productos
        productos = inventory_page.obtener_todos_los_productos()
        assert len(productos) > 0, "No hay productos en el inventario"
        
    finally:
        driver.quit()


@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_agregar_producto_al_carrito(login_in_driver, username, password):
    """Verifica que se pueda agregar un producto al carrito."""
    driver = login_in_driver(username, password)

    try:
        inventory_page = InventoryPage(driver)
        
        # Verificar carrito vacío al inicio
        assert inventory_page.obtener_conteo_carrito() == 0, "El carrito no está vacío al inicio"
        
        # Agregar un producto
        inventory_page.agregar_primer_producto(0)
        
        # Verificar que se agregó
        assert inventory_page.obtener_conteo_carrito() == 1, "El carrito no tiene 1 producto después de agregar"
        
    finally:
        driver.quit()


@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_producto_en_carrito(login_in_driver, username, password):
    """Verifica que el producto agregado aparezca en el carrito."""
    driver = login_in_driver(username, password)

    try:
        inventory_page = InventoryPage(driver)
        
        # Agregar primer producto
        inventory_page.agregar_primer_producto(0)
        
        # Abrir carrito
        inventory_page.abrir_carrito()
        
        # Validar el producto en el carrito
        cart_page = CartPage(driver)
        productos_carrito = cart_page.obtener_nombres_productos_carrito()
        assert len(productos_carrito) == 1, "El carrito no tiene el producto agregado"
        
    finally:
        driver.quit()
