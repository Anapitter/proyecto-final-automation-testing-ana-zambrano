from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException # Importa la excepción específica

class InventoryPage:
    """Clase Page Object para la página de Inventario de Sauce Labs."""
    
    # Selectors
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = (By.TAG_NAME, "button")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.ID, "shopping_cart_container")

    def __init__(self, driver):
        self.driver = driver
        # Inicializa WebDriverWait, usando el driver inyectado que ya no es None
        self.wait = WebDriverWait(driver, 10)

    # -------------------------
    # Obtener productos
    # -------------------------
    def obtener_todos_los_productos(self):
        """Espera y retorna todos los elementos de productos en la página."""
        return self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_ITEMS)
        )

    # -------------------------
    # Agregar por índice
    # -------------------------
    def agregar_primer_producto(self, indice=0):
        """Agrega un producto al carrito por su índice en la lista."""
        productos = self.obtener_todos_los_productos()
        producto = productos[indice]
        # Busca el botón DENTRO del elemento producto (scope local)
        boton = producto.find_element(*self.ADD_TO_CART_BUTTON)
        boton.click()

    # -------------------------
    # Agregar por nombre
    # -------------------------
    def agregar_producto_por_nombre(self, nombre_producto):
        """Agrega un producto al carrito buscando por su nombre."""
        productos = self.obtener_todos_los_productos()
        for producto in productos:
            nombre = producto.find_element(*self.PRODUCT_NAME).text
            if nombre == nombre_producto:
                boton = producto.find_element(*self.ADD_TO_CART_BUTTON)
                boton.click()
                return
        raise Exception(f"Producto '{nombre_producto}' no encontrado")

    # -------------------------
    # Contador del carrito (MEJORADO)
    # -------------------------
    def obtener_conteo_carrito(self):
        """Retorna el número de ítems en el carrito (el valor del badge)."""
        try:
            # Intentamos encontrar la insignia del carrito
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except NoSuchElementException:
            # Si el elemento 'CART_BADGE' no existe (carrito vacío), retornamos 0.
            return 0 
        except ValueError:
            # Si el texto del badge no puede convertirse a entero
            print("Advertencia: El contador del carrito no es un número válido.")
            return 0

    # -------------------------
    # Abrir carrito
    # -------------------------
    def abrir_carrito(self):
        """Hace clic en el icono del carrito para ir a la página del carrito."""
        icono = self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        )
        icono.click()