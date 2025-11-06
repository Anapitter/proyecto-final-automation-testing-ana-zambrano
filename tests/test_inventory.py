from selenium.webdriver.common.by import By
from selenium import webdriver

def test_inventory(login_in_driver):
    driver = login_in_driver
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0, "No se encontraron productos en el inventario"
