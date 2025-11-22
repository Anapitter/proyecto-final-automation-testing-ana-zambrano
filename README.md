# Proyecto Final - Automation Testing  

**Autora:** Ana Carolina Zambrano  
**Fecha:** Noviembre 2025  

Este proyecto contiene pruebas automatizadas **UI con Selenium + Pytest** y pruebas **API con Requests**, organizadas de forma modular y siguiendo buenas prácticas de automatización.

---

## 📁 Estructura del Proyecto

entrega-final-automation-testing/
│── utils/
│ ├── utils.py
│
│── tests/
│ ├── ui/
│ │ ├── test_login.py
│ │ ├── test_inventory.py
│ │ ├── test_cart.py
│ │ ├── test_cart_json.py
│ │ ├── test_login_faker.py
│ │
│ ├── api/
│ ├── test_api_get.py
│ ├── test_api_post.py
│ ├── test_api_delete.py
│
│── conftest.py
│── pytest.ini
│── README.md

---

## Tecnologías utilizadas  

- **Python 3.13**
- **Pytest 8**
- **Selenium 4**
- **Driver Chrome (ChromeDriver For Testing)**
- **Requests**
- **Faker**
- **pytest-html** (para reportes)

---

## Instalación

1. Crear entorno virtual:
python -m venv venv

2. Activarlo:
Windows:

venv\Scripts\activate

3.Instalar dependencias:
pip install -r requirements.txt

## Ejecutar las pruebas

## Todas las pruebas

pytest -v

pytest -v --html=report.html --self-contained-html

---

## Pruebas UI Selenium

Se automatizaron los siguientes flujos en **SauceDemo**:

✔ Login válido e inválido  
✔ Agregar productos al carrito  
✔ Validar inventario  
✔ Carrito con carga desde JSON  
✔ Login con datos generados con Faker  

Cada test utiliza un fixture en `conftest.py` que abre y cierra el navegador automáticamente.

---

## Pruebas API

Endpoints utilizados:

- **GET** https://reqres.in/api/users?page=2  
- **POST** https://jsonplaceholder.typicode.com/posts  
- **DELETE** https://reqres.in/api/users/2  

Validaciones:

✔ Código de estado  
✔ Claves del JSON  
✔ Longitud de listas  
✔ Creación de usuario (201)  
✔ Eliminación (204)

---

## Contacto

Para dudas o revisiones:  
**Ana Laura Zambrano** – entrega final Testing QA 