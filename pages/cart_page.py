from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    """Clase Page Object para la página del Carrito de Compras."""

    # Selectors
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def obtener_nombres_productos_carrito(self):
        """
        Espera a que los ítems del carrito estén visibles y retorna una lista
        con los nombres de todos los productos en el carrito.
        Si no hay ítems, retorna una lista vacía.
        """
        # Espera hasta 15 segundos a que los elementos del carrito sean visibles
        try:
            items = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_all_elements_located(self.CART_ITEMS)
            )
        except Exception:
            # Si no se encuentran ítems dentro del timeout, devolvemos lista vacía
            return []

        # Recorre cada ítem y extrae el texto del nombre del producto
        nombres = []
        for item in items:
            try:
                nombres.append(item.find_element(*self.ITEM_NAME).text)
            except Exception:
                # Saltar elementos que no tengan el nombre por cualquier razón
                continue
        return nombres
