# 🚀 Proyecto Final - Automation Testing

**Autora:** Ana Carolina Zambrano  
**Fecha:** Diciembre 2025  
**Descripción:** Proyecto integrador de pruebas automatizadas **UI con Selenium + Pytest** y pruebas **API con Requests**, organizadas bajo el patrón Page Object Model.

---

## 📋 Contenido

- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Tecnologías](#-tecnologías-utilizadas)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Ejecución de Pruebas](#-ejecución-de-pruebas)
- [Descripción de Tests](#-descripción-de-tests)
- [Reportes](#-reportes)

---

## 📁 Estructura del Proyecto

```
entrega-final-automation-testing-ana-zambrano/
│
├── conftest.py                 # Configuración de fixtures de pytest
├── pytest.ini                  # Archivo de configuración de pytest
├── requirements.txt            # Dependencias del proyecto
├── README.md                   # Este archivo
├── run_tests.py                # Script para ejecutar todas las pruebas
│
├── pages/                      # Page Objects para tests UI
│   ├── __init__.py
│   ├── login_page.py           # Página de login
│   ├── inventory_page.py       # Página de inventario
│   └── cart_page.py            # Página del carrito
│
├── tests/                      # Tests del proyecto
│   ├── __init__.py
│   ├── ui/                     # Tests de interfaz de usuario
│   │   ├── __init__.py
│   │   ├── test_login.py       # Tests de autenticación
│   │   ├── test_inventory.py   # Tests de inventario
│   │   ├── test_cart.py        # Tests del carrito
│   │   ├── test_cart_json.py   # Tests con datos desde JSON
│   │   └── test_login_faker.py # Tests con datos generados (Faker)
│   │
│   └── api/                    # Tests de API REST
│       ├── __init__.py
│       ├── test_api_get.py     # Test GET
│       ├── test_api_post.py    # Test POST
│       └── test_api_delete.py  # Test DELETE
│
├── utils/                      # Utilidades y helpers
│   ├── __init__.py
│   ├── datos.py                # Lectura de datos CSV
│   ├── lector_json.py          # Lectura de datos JSON
│   └── logger.py               # Configuración de logging
│
├── datos/                      # Archivos de datos
│   ├── data_login.csv          # Datos para tests de login
│   └── productos.json          # Catálogo de productos
│
├── assets/                     # Recursos estáticos
│   └── style.css               # Estilos (si aplica)
│
└── .gitignore                  # Archivos ignorados por Git
```

---

## 🛠 Tecnologías utilizadas

| Tecnología | Versión | Propósito |
|-----------|---------|----------|
| **Python** | 3.13+ | Lenguaje base |
| **Pytest** | 8.0+ | Framework de testing |
| **Selenium** | 4.15+ | Automatización UI |
| **WebDriver Manager** | 4.0+ | Gestión de ChromeDriver |
| **Requests** | 2.31+ | Testing de APIs REST |
| **Faker** | 20.0+ | Generación de datos aleatorios |
| **pytest-html** | 4.1+ | Reportes HTML |
| **python-dateutil** | 2.8+ | Utilidades de fechas |

---

## ✅ Requisitos

- Python 3.10 o superior
- Navegador Chrome instalado (para Selenium)
- Acceso a internet para descargar ChromeDriver automáticamente
- `pip` actualizado

---

## 📦 Instalación

### 1. Clonar el repositorio

\`\`\`bash
git clone https://github.com/Anapitter/proyecto-final-automation-testing-ana-zambrano.git
cd proyecto-final-automation-testing-ana-zambrano
\`\`\`

### 2. Crear entorno virtual

**Windows (PowerShell):**
\`\`\`powershell
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
\`\`\`

**Windows (CMD):**
\`\`\`cmd
python -m venv venv
venv\\Scripts\\activate.bat
\`\`\`

**macOS/Linux:**
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

### 3. Instalar dependencias

\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

## 🧪 Ejecución de Pruebas

### Ejecutar todas las pruebas

\`\`\`bash
pytest -v
\`\`\`

### Ejecutar con reporte HTML

\`\`\`bash
python run_tests.py
\`\`\`

O manualmente:

\`\`\`bash
pytest -v --html=reports/report.html --self-contained-html
\`\`\`

### Ejecutar solo pruebas UI

\`\`\`bash
pytest tests/ui/ -v
\`\`\`

### Ejecutar solo pruebas API

\`\`\`bash
pytest tests/api/ -v
\`\`\`

### Ejecutar un test específico

\`\`\`bash
pytest tests/ui/test_login.py -v
\`\`\`

### Ejecutar con log detallado

\`\`\`bash
pytest -v -s --log-cli-level=DEBUG
\`\`\`

---

## 📊 Descripción de Tests

### Tests UI (Selenium)

Se automatizaron flujos en **SauceDemo** (https://www.saucedemo.com/):

#### **test_login.py** - Autenticación
- ✅ Login válido con usuario estándar
- ✅ Login inválido (usuario bloqueado)
- ✅ Login con credenciales vacías
- ✅ Login con credenciales incorrectas
- Parametrizado con datos desde CSV

#### **test_inventory.py** - Gestión de Inventario
- ✅ Verificar disponibilidad de productos
- ✅ Carrito vacío al inicio
- ✅ Agregar producto al carrito
- ✅ Verificar contador de carrito
- ✅ Validar producto en el carrito

#### **test_cart.py** - Carrito de Compras
- ✅ Agregar producto al carrito
- ✅ Navegar al carrito
- ✅ Validar nombre del producto en el carrito

#### **test_cart_json.py** - Datos desde JSON
- ✅ Agregar primer producto del JSON
- ✅ Agregar múltiples productos del JSON
- Utiliza el archivo `datos/productos.json`

#### **test_login_faker.py** - Datos Aleatorios
- ✅ Login con usuarios generados dinámicamente (Faker)
- ✅ Validar mensaje de error esperado
- Genera nombres de usuario y contraseñas aleatorios

### Tests API (Requests)

#### **test_api_get.py**
- Endpoint: `GET https://reqres.in/api/users?page=2`
- Valida: Código de estado HTTP

#### **test_api_post.py**
- Endpoint: `POST https://reqres.in/api/users`
- Payload: `{"name": "Carolina", "job": "Automation Tester"}`
- Valida: Creación de usuario (201)

#### **test_api_delete.py**
- Endpoint: `DELETE https://reqres.in/api/users/2`
- Valida: Eliminación correcta (204)

---

## 📈 Reportes

Los reportes HTML se generan en la carpeta `reports/` con timestamp:

\`\`\`
reports/
├── report_20251210_145830.html
├── report_20251210_150030.html
└── ...
\`\`\`

Para abrir el reporte en el navegador:

\`\`\`bash
start reports/report_*.html  # Windows
open reports/report_*.html   # macOS
xdg-open reports/report_*.html # Linux
\`\`\`

---

## 📝 Características Principales

✨ **Page Object Model:** Separación clara entre localizadores y lógica de tests  
✨ **Fixtures Dinámicas:** Factory fixtures para reutilizar configuración  
✨ **Parametrización:** Tests parametrizados con CSV, JSON y generación dinámica  
✨ **Logging:** Sistema de logging con guardado en archivo y consola  
✨ **Screenshots:** Capturas automáticas en caso de fallos  
✨ **Reportes HTML:** Reportes detallados con pytest-html  

---

## 🐛 Solución de Problemas

### ChromeDriver no se descarga
- Asegúrate de tener Chrome instalado
- Verifica conexión a internet
- Intenta: `webdriver-manager clean`

### Problema con permisos de ejecución en macOS/Linux
\`\`\`bash
chmod +x run_tests.py
\`\`\`

### El JSON de productos no se encuentra
- Verifica que `datos/productos.json` existe
- Comprueba la ruta relativa desde la carpeta raíz

---

## 👨‍💻 Autor

**Ana Carolina Zambrano**  
[GitHub](https://github.com/Anapitter)

---

## 📄 Licencia

Este proyecto es parte de un curso de automatización testing. Uso educativo únicamente.

## Contacto

Para dudas o revisiones:  
**Ana Laura Zambrano** – entrega final Testing QA 