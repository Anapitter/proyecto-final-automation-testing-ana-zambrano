import pytest
from selenium import webdriver
from pages.login_page import LoginPage # Asegúrate de que esta importación sea correcta

# --- Fixture 1: Inicialización y Cierre del Driver ---
@pytest.fixture(scope="function")
def driver():
    # Es recomendable usar WebDriver Manager para la gestión automática del driver
    # from selenium.webdriver.chrome.service import Service as ChromeService
    # from webdriver_manager.chrome import ChromeDriverManager
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    driver = webdriver.Chrome() # Usa esta línea si el binario de Chrome está en tu PATH
    driver.maximize_window()
    yield driver
    driver.quit()

# --- Fixture 2: Página de Login (Depende del Driver) ---
@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)

# --- Fixture 3: Función de Login (CORREGIDA) ---
# Debe retornar el objeto WebDriver para que los tests lo utilicen.
@pytest.fixture(scope="function")
def login_in_driver(login_page, driver): # driver se inyecta desde la fixture 'driver'
    
    def login(usuario, password):
        # 1. Abre la página usando la Page Object
        login_page.abrir_pagina()
        
        # 2. Realiza el login
        login_page.login_completo(usuario, password)
        
        # 3. ¡IMPORTANTE! Retornar el objeto driver real después de la acción.
        return driver 
        
    return login