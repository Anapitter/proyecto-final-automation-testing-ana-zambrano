# 🔧 Guía de Configuración — VS Code + Autocompletado

## ✅ Estado Actual

Tu proyecto está **correctamente configurado** para:

- ✨ Autocompletado inteligente con Pylance
- 🎯 Terminal Git Bash integrada
- 📦 Gestión automática de dependencias Python
- 🔍 Análisis de código en tiempo real

---

## 📋 Pasos para Activar Autocompletado

### 1️⃣ Instalar Extensiones Recomendadas

Cuando abras el proyecto en VS Code, verás una notificación en la esquina inferior derecha:

> "This workspace has extension recommendations"

**Haz clic en "Install All"** para instalar:

- `Python` (Microsoft)
- `Pylance` (Microsoft)

O instala manualmente:

1. Abre la paleta de comandos: `Ctrl + Shift + P`
2. Escribe: `Extensions: Install from Recommended`
3. Presiona Enter

---

### 2️⃣ Seleccionar el Intérprete Python Correcto

1. Abre la paleta de comandos: `Ctrl + Shift + P`
2. Escribe: `Python: Select Interpreter`
3. Busca y elige:

   ```text
   ./venv/Scripts/python.exe
   ```

   (O la carpeta `venv` en tu proyecto)

**Alternativa visual:**

- Mira la esquina inferior derecha de VS Code
- Haz clic donde dice "Python 3.x.x"
- Selecciona el intérprete `./venv/Scripts/python.exe`

---

### 3️⃣ Reiniciar VS Code

Después de instalar Pylance:

1. Cierra VS Code completamente
2. Abre nuevamente el proyecto
3. Espera a que Pylance se inicialice (verás "Pylance" en la esquina inferior)

---

## ✨ Características Activadas

Una vez completados los pasos anteriores, tendrás:

### 🎯 Autocompletado Inteligente

- Presiona `Ctrl + Space` en cualquier editor para ver sugerencias
- Las sugerencias aparecen automáticamente mientras escribes

### 📚 Información de Funciones

- Pasa el ratón sobre cualquier función para ver su documentación
- Pylance mostrará parámetros y tipos automáticamente

### 🔍 Análisis de Errores en Tiempo Real

- Errores de sintaxis subrayan en rojo
- Importaciones no resueltas aparecen destacadas

### 🎨 Formato Automático

- `formatOnSave` activado: se formatea al guardar (`Ctrl + S`)
- `formatOnType` activado: se formatea mientras escribes

---

## 🧪 Prueba el Autocompletado

1. Abre cualquier archivo Python (ej: `pages/login_page.py`)
2. Escribe:

   ```python
   from selenium
   ```

3. Presiona `Ctrl + Space`
4. Deberías ver sugerencias de `selenium`

5. Escribe más:

   ```python
   from selenium.webdriver.common.by import By
   ```

6. Al escribir `By.`, presiona `Ctrl + Space` y verás todas las opciones

---

## 🔌 Terminal Git Bash Integrada

VS Code ahora abre **Git Bash** por defecto:

1. Presiona `` Ctrl + ` `` para abrir la terminal integrada
2. Deberías ver `bash-x.y.z$` en lugar de PowerShell
3. Puedes ejecutar comandos bash directamente:

   ```bash
   python run_tests.py
   pytest -v
   git status
   ```

---

## 🐛 Solución de Problemas

### Pylance no aparece en la esquina inferior

1. Abre la paleta: `Ctrl + Shift + P`
2. Escribe: `Python: Show Logs`
3. Revisa si hay errores de instalación
4. Si necesario, reinstala Pylance:
   - `Ctrl + Shift + X` (extensiones)
   - Busca "Pylance"
   - Haz clic en "Reinstall"

### El autocompletado no funciona

1. Verifica que el intérprete correcto está seleccionado (esquina inferior derecha)
2. Abre un archivo `.py` (no funciona en markdown)
3. Presiona `Ctrl + Space` en el editor
4. Si aún no funciona, reinicia VS Code

### Git Bash no aparece en terminal

1. Abre una nueva terminal: `` Ctrl + ` ``
2. Si sigue siendo PowerShell, haz clic en el dropdown `+` → "Git Bash"
3. Si no aparece "Git Bash", verifica que Git esté instalado en `C:\Program Files\Git`

---

---

## 📖 Referencias

- [Documentación de Pylance](https://github.com/microsoft/pylance-release)
- [Documentación de Python en VS Code](https://code.visualstudio.com/docs/languages/python)
- [Git Bash en VS Code](https://code.visualstudio.com/docs/editor/integrated-terminal#_configuration)

---

## ✅ Verificación Rápida

Para confirmar que todo está configurado correctamente, ejecuta en Git Bash:

```bash
python --version
pytest --version
git --version
```

Deberías ver versiones sin errores.

---

**¡Listo!** Ahora tienes un entorno de desarrollo completamente configurado con autocompletado inteligente, formateo automático y terminal Git Bash integrada. 🚀

