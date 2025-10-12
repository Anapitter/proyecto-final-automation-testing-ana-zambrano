# utils/funciones.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def abrir_navegador():
    """Abre Chrome maximizado y devuelve el driver."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def login_saucedemo(driver, usuario="standard_user", clave="secret_sauce"):
    """Hace login en SauceDemo con usuario y clave indicados."""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(clave)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)  # Pequeña espera para que cargue la página

def cerrar_navegador(driver):
    """Cierra el navegador."""
    driver.quit()
    
def agregar_producto_carrito(driver, indice=0):
    """
    Agrega un producto al carrito.
    :param driver: driver de Selenium
    :param indice: índice del producto a agregar (por defecto 0)
    :return: nombre y precio del producto agregado
    """
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    boton_agregar = productos[indice].find_element(By.TAG_NAME, "button")
    boton_agregar.click()

    nombre = productos[indice].find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = productos[indice].find_element(By.CLASS_NAME, "inventory_item_price").text
    return nombre, precio