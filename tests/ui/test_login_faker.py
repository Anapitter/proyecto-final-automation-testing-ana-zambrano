from selenium.webdriver.support.ui import WebDriverWait
import pytest
from faker import Faker
from pages.login_page import LoginPage # <--- ¡IMPORTANTE! Importar el Page Object


fake = Faker()

# Las credenciales de Faker siempre fallarán en Sauce Labs.
# Por lo tanto, ambos casos deben esperar 'False' para 'debe_funcionar'.
@pytest.mark.parametrize(
    "usuario,password,debe_funcionar",
    [
        # Caso 1: Usuario/Contraseña de Faker -> Esperamos FALLO
        (fake.user_name(), fake.password(), False),
        # Caso 2: Usuario/Contraseña de Faker -> Esperamos FALLO
        (fake.user_name(), fake.password(), False) 
        # Si quieres probar el ÉXITO, debes usar un usuario válido fijo aquí,
        # ej: ("standard_user", "secret_sauce", True)
    ]
)
def test_login_validation(login_in_driver, usuario, password, debe_funcionar):

    # login_in_driver siempre retorna el objeto WebDriver.
    driver = login_in_driver(usuario, password) 

    if debe_funcionar:
        # Este bloque solo se ejecutaría si hubieras puesto 'True' arriba.
        # El test fallaba porque el driver no se redirigía a inventory.html.
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario (Login fallido inesperadamente)"

    else:
        # El login falló, el driver sigue en la página de login.
        
        # 1. Verificar que no fuimos redirigidos.
        assert "/inventory.html" not in driver.current_url, "Se redirigió al inventario cuando no debía (Login exitoso inesperadamente)"
        
        # 2. Crea la instancia de LoginPage para poder usar su método.
        # La variable 'driver' NO es la Page Object; es el objeto WebDriver.
        login_page = LoginPage(driver) 
        
        # 3. Llama al método Page Object
        mensaje = login_page.obtener_mensaje_error()
        
        # 4. Aserción final (usando el texto real para mayor robustez)
        assert "Epic sadface" in mensaje, f"El mensaje de error esperado no se encontró. Obtenido: {mensaje}"