# Proyecto Final - Framework de Automatización de Pruebas

**Autora:** Ana Laura Zambrano

**Fecha:** Diciembre 2025

**Repositorio:** [proyecto-final-automation-testing-ana-zambrano](https://github.com/Anapitter/proyecto-final-automation-testing-ana-zambrano)

## Propósito del Proyecto

Este proyecto constituye un **framework completo de automatización de pruebas** que integra todos los conocimientos adquiridos en el curso de Testing & QA. El objetivo es demostrar:

Automatización robusta de **Pruebas UI** con Selenium WebDriver  
Automatización completa de **Pruebas de API** con Requests  
Aplicación del patrón **Page Object Model**  
Implementación de **buenas prácticas** de código  
Generación de **reportes visuales** detallados  
Gestión profesional con **Git y GitHub**  

---

## Tabla de Contenidos

- Propósito del Proyecto
- Tabla de Contenidos
- Tecnologías Utilizadas
- Estructura del Proyecto
- Requisitos Previos
- Instalación
- Ejecución de Pruebas
- Pruebas UI
- Pruebas API
- Reportes HTML
- Sistema de Logging
- Capturas de Pantalla
- Solución de Problemas
- Contacto

---

## Estructura del Proyecto

entrega-final-automation-testing-ana-zambrano/
│
├── conftest.py                 # Configuración de fixtures de pytest
├── pytest.ini                  # Archivo de configuración de pytest
├── requirements.txt            # Dependencias del proyecto
├── README.md                   # Este archivo
├── run_tests.py                # Script para ejecutar todas las pruebas
│
├── pages/                      # Page Objects para tests UI
│   ├── _init_.py
│   ├── login_page.py           # Página de login
│   ├── inventory_page.py       # Página de inventario
│   └── cart_page.py            # Página del carrito
│
├── tests/                      # Tests del proyecto
│   ├── _init_.py
│   ├── ui/                     # Tests de interfaz de usuario
│   │   ├── _init_.py
│   │   ├── test_login.py       # Tests de autenticación
│   │   ├── test_inventory.py   # Tests de inventario
│   │   ├── test_cart.py        # Tests del carrito
│   │   ├── test_cart_json.py   # Tests con datos desde JSON
│   │   └── test_login_faker.py # Tests con datos generados (Faker)
│   │
│   └── api/                    # Tests de API REST
│       ├── _init_.py
│       ├── test_api_get.py     # Test GET
│       ├── test_api_post.py    # Test POST
│       └── test_api_delete.py  # Test DELETE
│
├── utils/                      # Utilidades y helpers
│   ├── _init_.py
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

---

## Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|:--|:--|:--|
| **Python** | 3.12+ | Lenguaje de programación base |
| **Pytest** | 8.0+ | Framework de testing principal |
| **Selenium** | 4.15+ | Automatización de UI (web) |
| **WebDriver Manager** | 4.0+ | Gestión automática de ChromeDriver |
| **Requests** | 2.31+ | Testing de APIs REST |
| **pytest-html** | 4.1+ | Generación de reportes HTML |
| **pytest-metadata** | 3.0+ | Metadatos en reportes |
| **Faker** | 20.0+ | Generación de datos aleatorios |
| **python-dateutil** | 2.8+ | Utilidades de fecha/hora |
| **Git** | 2.0+ | Control de versiones |

---

## Requisitos Previos

- Python 3.12 o superior
- Navegador Chrome instalado (para Selenium)
- Acceso a internet para descargar ChromeDriver automáticamente
- Git instalado
- `pip` actualizado

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Anapitter/proyecto-final-automation-testing-ana-zambrano.git
cd proyecto-final-automation-testing-ana-zambrano
```

### 2. Crear entorno virtual

Se recomienda usar el nombre de entorno `.venv` (coincide con el `.gitignore` del proyecto).

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Abrir Git Bash en el Repositorio

Se incluyen dos scripts para abrir Git Bash automáticamente desde el repositorio:

### Opción 1: Windows Batch (CMD)

```bash
open_in_gitbash.bat
```

### Opción 2: PowerShell

```powershell
.\open_in_gitbash.ps1
```

Si ves un error de permisos en PowerShell, ejecuta primero:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Luego ejecuta nuevamente el script.

---

## Ejecución de Pruebas

### Ejecutar todas las pruebas

```bash
pytest -v
```

### Ejecutar con reporte HTML

```bash
python run_tests.py
```

O manualmente:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

### Ejecutar solo pruebas UI

```bash
pytest tests/ui/ -v
```

### Ejecutar solo pruebas API

```bash
pytest tests/api/ -v
```

### Ejecutar un test específico

```bash
pytest tests/ui/test_login.py -v
```

### Ejecutar con log detallado

```bash
pytest -v -s --log-cli-level=DEBUG
```

---

## Pruebas UI — Selenium WebDriver

### Sitio Web Automatizado

**SauceDemo:** [saucedemo.com](https://www.saucedemo.com/)

Se han automatizado **5+ casos de prueba** cubriendo flujos completos:

### 1. **test_login.py** — Autenticación (4 casos)

Parametrizado con datos desde `datos/data_login.csv`:

| Caso | Usuario | Contraseña | Resultado Esperado |
|:--|:--|:--|:--|
| 1 | `standard_user` | `secret_sauce` |  Login exitoso |
| 2 | `locked_out_user` | `secret_sauce` |  Usuario bloqueado |
| 3 | (vacío) | (vacío) |  Credenciales requeridas |
| 4 | `invalid_user` | `invalid_pass` |  Credenciales incorrectas |

**Implementación:**

- Uso de fixture `login_in_driver` (patrón _factory_ / factory pattern)
- Validación de mensajes de error
- Captura automática en fallos

### 2. **test_inventory.py** — Gestión de Inventario (3 casos)

- **test_inventory_productos_disponibles:** Verifica que hay productos disponibles
- **test_agregar_producto_al_carrito:** Agrega el primer producto
- **test_producto_en_carrito:** Valida que el producto está en el carrito

**Características:**

- Flujo completo: login → inventario → carrito
- Validación de contador de carrito
- Parametrizado con múltiples usuarios

### 3. **test_cart.py** — Carrito de Compras (1 caso)

- Agrega producto y valida en el carrito

### 4. **test_cart_json.py** — Datos desde JSON (2 casos)

Carga datos desde `datos/productos.json`:

```json
[
  {"name": "Sauce Labs Backpack", "description": "..."},
  {"name": "Sauce Labs Bike Light", "description": "..."},
  {"name": "Sauce Labs Bolt T-Shirt", "description": "..."}
]
```

- **Caso 1:** Agrega primer producto del JSON
- **Caso 2:** Agrega múltiples productos del JSON

**Implementación:**

- Fixture `productos_json` que carga el archivo
- Lectura mediante `utils/lector_json.py`
- Validación en carrito

### 5. **test_login_faker.py** — Datos Aleatorios (2 casos)

Genera credenciales dinámicamente usando **Faker**:

```python
usuario = fake.name()        # Nombre aleatorio
password = fake.password()   # Contraseña aleatoria
```

- **Caso 1:** Login con usuario aleatorio (debe fallar)
- **Caso 2:** Validación de mensaje de error "Epic sadface"

**Implementación:**

- Generador de datos dinámicos
- Sin necesidad de archivos de datos
- Prueba robustez del sistema

---

## Patrón Page Object Model (POM)

La estructura **pages/** implementa el patrón POM para máxima mantenibilidad:

### **LoginPage** (`pages/login_page.py`)

```python
class LoginPage:
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _BUTTON_LOGIN = (By.ID, "login-button")
    
    def completar_user(self, usuario):
        """Rellenar campo de usuario"""
    
    def completar_pass(self, password):
        """Rellenar campo de contraseña"""
    
    def hacer_click_button(self):
        """Hacer clic en botón login"""
```

### **InventoryPage** (`pages/inventory_page.py`)

```python
class InventoryPage:
    def obtener_todos_los_productos(self):
        """Retorna lista de productos"""
    
    def agregar_producto_por_nombre(self, nombre):
        """Agrega producto específico al carrito"""
```

### **CartPage** (`pages/cart_page.py`)

```python
class CartPage:
    def obtener_nombres_productos_carrito(self):
        """Retorna nombres de productos en carrito"""
```

**Beneficios:**

-Reutilización de código
-Fácil mantenimiento
-Cambios en UI sin afectar tests
-Mejor legibilidad

---

## Pruebas API — Requests

### API Pública Utilizada

**ReqRes:** [reqres.in](https://reqres.in/)

Se implementaron **3 casos de prueba** con diferentes métodos HTTP:

### 1. **test_api_get.py** — GET

```http
GET https://reqres.in/api/users?page=2
```

**Validaciones:**

- Código de estado HTTP (200 o 403)
- Estructura de respuesta JSON
- Presencia de datos de usuario

### 2. **test_api_post.py** — POST

```http
POST https://reqres.in/api/users
Content-Type: application/json

{
  "name": "Carolina",
  "job": "Automation Tester"
}
```

**Validaciones:**

- Creación de recurso (201)
- ID asignado en respuesta
- Timestamp de creación

### 3. **test_api_delete.py** — DELETE

```http
DELETE https://reqres.in/api/users/2
```

**Validaciones:**

- Eliminación correcta (204)
- Sin contenido en respuesta

---

## Reportes HTML

Los reportes se generan con **pytest-html** en la carpeta `reports/`:

### Nombre de Archivo

```text
report_YYYYMMDD_HHMMSS.html
Ejemplo: report_20251210_231018.html
```

### Contenido del Reporte

- Resumen general (total, pasados, fallidos, skipped)
- Detalle de cada test (duración, estado)
- Screenshots para pruebas fallidas
- Logs y trazas de error
- Timestamp de ejecución

### Abrir el Reporte

```bash
# Windows
start reports/report_20251210_231018.html

# macOS
open reports/report_20251210_231018.html

# Linux
xdg-open reports/report_20251210_231018.html
```

---

## Sistema de Logging

Implementado en `utils/logger.py` con configuración centralizada:

### Niveles de Log

- **CRITICAL:** Errores críticos del sistema
- **ERROR:** Errores en ejecución
- **WARNING:** Advertencias
- **INFO:** Información general (default console)
- **DEBUG:** Detalles técnicos (default file)

### Almacenamiento

```text
logs/
├── app_2025-12-10_23-10-18.log
├── app_2025-12-10_23-12-45.log
└── ...
```

### Uso en Tests

```python
from utils.logger import logger

logger.info("Iniciando login con usuario: standard_user")
logger.debug("WebDriver esperando elemento: user-name")
logger.error("Elemento no encontrado: login-button")
```

---

## Capturas de Pantalla

Implementadas en `conftest.py` con hook de pytest:

### Funcionamiento

- Se captura automáticamente cuando un test **falla**
- Se almacena en carpeta `screenshots/`
- Nombre descriptivo con timestamp y nombre del test
- Se incluye en el reporte HTML

### Estructura

```text
screenshots/
├── test_login_validation_20251210_231018.png
├── test_agregar_producto_al_carrito_20251210_231020.png
└── ...
```

---

## Control de Versiones con Git

El proyecto mantiene un historial limpio de commits documentando el progreso:

### Estructura de Commits

```bash
git log --oneline
```

Ejemplo:

```text
312cdd1 docs: fix SETUP.md markdown lint errors
e1a2b3c docs: add SETUP.md with VS Code configuration
7f6e5d4 chore: workspace settings and Git Bash integration
```

### Ramas

- `main` — Rama principal con código estable
- Historial de development commits documentado

---

## Requisitos Cumplidos de la Consigna

### Tecnologías Usadas

- **Python** — Lenguaje principal
- **Pytest** — Framework de testing
- **Selenium WebDriver** — Automatización UI
- **Requests** — Testing de APIs
- **Git/GitHub** — Control de versiones

### Organización del Código

- Estructura clara con directorios: pages/, tests/, utils/, datos/
- **Page Object Model (POM)** implementado
- Buenas prácticas de programación
- Comentarios descriptivos en todo el código
- Nombres significativos en variables, métodos y clases

### Pruebas de UI (Selenium)

- **5+ casos de prueba** (test_login, test_inventory, test_cart, test_cart_json, test_login_faker)
- Flujos completos: login → navegación → carrito → checkout
- Escenarios negativos: login con credenciales inválidas, usuario bloqueado
- **Parametrización:** Datos desde CSV (`datos/data_login.csv`)
- **Múltiples fuentes:** CSV, JSON (`datos/productos.json`), Faker
- **Page Object Model:** Clases LoginPage, InventoryPage, CartPage
- **Capturas automáticas:** Screenshots en fallos con timestamp

### Pruebas de API

- **3+ casos de prueba** (GET, POST, DELETE)
- API pública ReqRes
- Métodos HTTP cubiertos: GET, POST, DELETE
- Validación de códigos de estado HTTP
- Validación de estructura JSON
- Assertions para múltiples escenarios

### Reportes

- **Reportes HTML detallados** con pytest-html
- Muestra: tests ejecutados, estado (pasado/fallado), duración
- **Capturas de pantalla en fallos** incluidas en reportes
- **Logging completo** con manejadores de archivo y consola

### Logging

- **Sistema centralizado** en `utils/logger.py`
- Registra pasos clave durante ejecución
- Nivel DEBUG detallado para debugging
- Archivos con timestamp en carpeta `logs/`

### Documentación

- **README.md completo** con:
  - Propósito del proyecto
  - Tecnologías utilizadas
  - Estructura del proyecto
  - Cómo instalar dependencias
  - Cómo ejecutar pruebas
  - Cómo interpretar reportes
  - Solución de problemas

### Control de Versiones

- **Repositorio en GitHub público**
- Historial de commits documentado
- Rama principal `main` con código estable
- Nombre de repositorio según consigna: `proyecto-final-automation-testing-ana-zambrano`

### Funcionalidad Esperada

- Todas las pruebas ejecutan consistentemente
- Pruebas independientes entre sí
- Reportes claros y detallados
- Estructura facilita agregar nuevas pruebas
- Código reutilizable y mantenible

--

Ver la sección **Reportes HTML** (más arriba) para detalles sobre la generación y apertura de reportes.

---

## Características Principales

- **Page Object Model:** Separación clara entre localizadores y lógica de tests
- **Fixtures Dinámicas:** Factory fixtures para reutilizar configuración
- **Parametrización:** Tests parametrizados con CSV, JSON y generación dinámica
- **Logging:** Sistema de logging con guardado en archivo y consola
- **Screenshots:** Capturas automáticas en caso de fallos
- **Reportes HTML:** Reportes detallados con pytest-html

---

## Solución de Problemas

### ChromeDriver no se descarga

**Problema:** `WebDriverException: unknown error: Chrome version X is not available`

**Solución:**

1. Asegúrate de tener **Chrome instalado**
2. Verifica **conexión a internet**
3. Limpia la caché de `webdriver-manager` (WebDriver Manager usa `.wdm` en el home):

- Windows (PowerShell):

  ```powershell
  Remove-Item -Recurse -Force $env:USERPROFILE\.wdm
  ```

4.Reinstala/actualiza el package si fuera necesario:

  ```bash
  pip install --upgrade webdriver-manager
  ```

### Problema con permisos de ejecución en macOS/Linux

**Solución:**

```bash
chmod +x run_tests.py
# Si tiene un script shell para abrir Git Bash en macOS/Linux: hacerlo ejecutable
# chmod +x open_in_gitbash.sh
```

### El archivo JSON de productos no se encuentra

**Problema:** `FileNotFoundError: [Errno 2] No such file or directory`

**Solución:**

1. Verifica que `datos/productos.json` existe
2. Comprueba la ruta relativa desde la carpeta raíz del proyecto
3. Asegúrate de que el nombre es exacto (sensible a mayúsculas)

### Tests fallan por timeout

**Problema:** `TimeoutException: Message: timeout`

**Solución:**

1. Aumenta el tiempo de espera en `conftest.py`:

   ```python
   self.wait = WebDriverWait(driver, 20)  # Aumentar de 10 a 20
   ```

2. Verifica que el sitio web está accesible
3. Intenta con más conexión a internet

### Git Bash no se abre con los scripts

**Problema:** `open_in_gitbash.bat` o `.ps1` no funcionan

**Solución:**

1. Verifica que Git está instalado en `C:\Program Files\Git`
2. O modifica la ruta en el script según tu instalación:

   ```powershell
   # PowerShell
   $gitBashPath = "C:\Program Files\Git\git-bash.exe"
   ```

3. En PowerShell, permite ejecución de scripts:

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

---

## Contacto e Información del Autor

**Nombre:** Ana Laura Zambrano

**GitHub:** [Anapitter](https://github.com/Anapitter)

**Repositorio:** [proyecto-final-automation-testing-ana-zambrano](https://github.com/Anapitter/proyecto-final-automation-testing-ana-zambrano)

---

## Licencia

Este proyecto es parte del curso de **Automatización Testing & QA** y está disponible para uso educativo.

**Fecha de entrega:** Diciembre 2025

---

## Habilidades Demostradas

- Automatización de pruebas UI con Selenium
- Testing de APIs REST
- Patrones de diseño (Page Object Model)
- Fixtures y parametrización en Pytest
- Generación de reportes visuales
- Sistema de logging profesional
- Control de versiones con Git
- Documentación técnica completa
- Buenas prácticas de desarrollo
- Testing independiente y robusto
