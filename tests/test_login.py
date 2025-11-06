from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

@pytest.mark.parametrize("usuario,password", [
    ("standard_user", "secret_sauce"),
    ("admin", "1234")
])

def test_login_validation(login_in_driver, usuario, password):
        driver = login_in_driver(usuario,password)

        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"

    