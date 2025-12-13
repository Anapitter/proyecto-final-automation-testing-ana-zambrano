import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os

# Carpeta de capturas (usar la carpeta `Screenshot` para evidencias solicitada por el usuario)
SCREENSHOT_DIR = os.path.join(os.getcwd(), "Screenshot")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.fixture
def driver(request):
    """
    Fixture principal para inicializar y cerrar el WebDriver.
    Asegura que el navegador se cierre después de cada test.
    """
    chrome_options = Options()
    # Usamos una opción condicional para no maximizar si se usa un entorno headless
    # Esto ayuda a asegurar la máxima compatibilidad.
    # Puedes descomentar la siguiente línea si deseas forzar la maximización:
    # chrome_options.add_argument("--start-maximized") 
    
    service = Service(ChromeDriverManager().install())
    current_driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Usamos yield para que el driver esté disponible para los tests
    yield current_driver
    
    # Después de que el test termina (finalizer)
    current_driver.quit()

@pytest.fixture
def login_in_driver(driver):
    """
    Fixture que actúa como una Función Factory (High-Order Fixture).
    Devuelve una función que ejecuta el proceso de login en el WebDriver inyectado.
    Esto permite pasar usuario y contraseña dinámicamente desde los tests parametrizados.
    """
    def _login_function(username, password):
        # El driver ya está inicializado y gestionado por el fixture 'driver'
        driver.get("https://www.saucedemo.com/")
        
        # Realizar el login
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        
        # Devolver el driver ya autenticado
        return driver
        
    return _login_function # <-- DEVOLVEMOS LA FUNCIÓN DE LOGIN

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook de Pytest para tomar capturas de pantalla en caso de fallo en el test."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        # Intentamos obtener el driver del contexto del test
        driver = item.funcargs.get("driver")
        
        if driver:
            try:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                # Sanitizamos el nombre del test para el nombre del archivo
                test_name = item.nodeid.replace("::", "_").replace("[", "_").replace("]", "")
                file_path = os.path.join(SCREENSHOT_DIR, f"{test_name}_{timestamp}.png")
                
                # Guarda la captura de pantalla
                driver.save_screenshot(file_path)
                print(f"\n📸 Captura de pantalla guardada en: {file_path}")
            except Exception as e:
                # Captura y reporta errores al intentar tomar la captura
                print(f"\n[ERROR] No se pudo tomar la captura de pantalla: {e}")

# Añadir configuraciones comunes (si tienes Page Objects, etc.)
# Por ejemplo, puedes definir un fixture para la URL base aquí si es necesario.