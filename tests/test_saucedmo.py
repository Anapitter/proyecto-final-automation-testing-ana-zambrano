# tests/test_saucedemo.py
from utils.funciones import abrir_navegador, login_saucedemo, cerrar_navegador, agregar_producto_carrito
from utils.funciones import abrir_navegador, login_saucedemo, cerrar_navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_exitoso():
    driver = abrir_navegador()
    login_saucedemo(driver)

    # Validar URL
    assert "/inventory.html" in driver.current_url

    # Validar título
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == "Products"
    print("Login exitoso y página de inventario cargada.")

    cerrar_navegador(driver)

def test_login_invalido():
    driver = abrir_navegador()
    login_saucedemo(driver, usuario="usuario_invalido", clave="clave_invalida")

    # Verificar mensaje de error
    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    print("Mensaje de error:", error)
    assert "Epic sadface" in error  # Valida que sea el error esperado

    cerrar_navegador(driver)

def test_verificar_catalogo():
    driver = abrir_navegador()
    login_saucedemo(driver)

    # Validar título de inventario
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == "Products"
    
    # Validar presencia de al menos un producto
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0
    
    primer_producto = productos[0]
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    print("Primer producto:", nombre, "Precio:", precio)

    cerrar_navegador(driver)
    

def test_agregar_carrito():
    driver = abrir_navegador()
    login_saucedemo(driver)

    # Agregar primer producto
    nombre, precio = agregar_producto_carrito(driver)
    print("Producto agregado al carrito:", nombre, precio)

    # Ir al carrito y validar que el producto está presente
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    item_carrito = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )
    assert item_carrito.text == nombre
    print("Producto validado en el carrito correctamente:", item_carrito.text)

    cerrar_navegador(driver)



