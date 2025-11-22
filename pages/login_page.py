from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException

class LoginPage:
    """Clase que representa la página de inicio de sesión de Sauce Demo."""

    # URL
    URL = "https://www.saucedemo.com/"

    # Localizadores
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _BUTTON_LOGIN = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    def __init__(self, driver):
        """Inicializa la página de login."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        """Abre la página de inicio de sesión."""
        self.driver.get(self.URL)
        return self

    def completar_user(self, usuario):
        """Completa el campo de usuario."""
        try:
            input_element = self.wait.until(EC.element_to_be_clickable(self._USER_INPUT))
            input_element.clear()
            input_element.send_keys(usuario)
            return self
        except TimeoutException:
            raise Exception("El campo de usuario no está disponible")

    def completar_pass(self, password):
        """Completa el campo de contraseña."""
        try:
            input_element = self.wait.until(EC.element_to_be_clickable(self._PASS_INPUT))
            input_element.clear()
            input_element.send_keys(password)
            return self
        except TimeoutException:
            raise Exception("El campo de contraseña no está disponible")

    def hacer_click_button(self):
        """Hace clic en el botón de inicio de sesión."""
        try:
            button = self.wait.until(EC.element_to_be_clickable(self._BUTTON_LOGIN))
            button.click()
            return self
        except (TimeoutException, ElementNotInteractableException):
            raise Exception("El botón de login no está disponible")

    def login_completo(self, usuario, password):
        """Realiza el proceso completo de inicio de sesión."""
        self.completar_user(usuario)
        self.completar_pass(password)
        self.hacer_click_button()
        return self

    def obtener_mensaje_error(self):
        """Obtiene el mensaje de error si aparece."""
        try:
            error = self.wait.until(EC.presence_of_element_located(self._ERROR_MESSAGE))
            return error.text
        except TimeoutException:
            return None

    def is_login_exitoso(self):
        """Verifica si el login fue exitoso."""
        return "/inventory.html" in self.driver.current_url
