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
        Espera a que los ítems del carrito estén presentes y retorna una lista
        con los nombres de todos los productos en el carrito.
        """
        # Espera hasta 10 segundos a que todos los elementos del carrito estén presentes
        items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.CART_ITEMS)
        )

        # Recorre cada ítem y extrae el texto del nombre del producto
        return [item.find_element(*self.ITEM_NAME).text for item in items]
