from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from utils.datos import leer_datos_csv

# Cargar datos desde el CSV en la carpeta `datos`
DATA_LOGIN = leer_datos_csv('datos/data_login.csv')

@pytest.mark.parametrize("usuario,password,expected_result", DATA_LOGIN)
def test_login_validation(login_in_driver, usuario, password, expected_result):
    """
    Prueba diferentes escenarios de inicio de sesión.
    
    Args:
        login_in_driver: Fixture que proporciona la función de login
        usuario: Nombre de usuario a probar
        password: Contraseña a probar
        expected_result: True si se espera login exitoso, False si se espera error
    """
    driver = login_in_driver(usuario, password)
    wait = WebDriverWait(driver, 10)
    
    if expected_result:
        # Verificar login exitoso
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
        
        # Verificar elementos de la página de inventario
        inventory_container = wait.until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        assert inventory_container.is_displayed(), "El contenedor del inventario no está visible"
    else:
        # Verificar que permanecemos en la página de login
        assert "/inventory.html" not in driver.current_url, "Se redirigió al inventario cuando no debería"
        
        # Verificar mensaje de error
        error_message = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        assert error_message.is_displayed(), "No se muestra el mensaje de error"
