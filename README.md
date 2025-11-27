# 🌐 **Proyecto – Calidad de Software (DUOC UC)**

Este repositorio corresponde al ramo **Calidad de Software** del Instituto Profesional **DUOC UC**, donde se trabajan prácticas de:

✔️ Validación
✔️ Automatización
✔️ Aseguramiento de Calidad

Esto mediante la ejecución de **pruebas automatizadas con Selenium** para evaluar el correcto funcionamiento de una aplicación web.

El proyecto está compuesto por **cuatro módulos de automatización**, cada uno orientado a un flujo clave: inicio de sesión, registro, compras y gestión del carrito.

---

## 📁 **Estructura del Repositorio**

### 🔐 **`inicio_sesion.py`**

Automatiza el flujo completo de **registro + inicio de sesión**.
Primero registra al usuario y luego utiliza esos mismos datos para validar correctamente el acceso.

---

### 🧑‍💻 **`registro_usuario.py`**

Simula el registro de un nuevo usuario, validando campos, mensajes del sistema y el almacenamiento de información.

---

### 🛒 **`compras_carrito.py`**

Simula la **selección y compra de productos**.
Este flujo **no requiere autenticación**, por lo que puede ejecutarse sin iniciar sesión.

---

### 🛍️ **`modificacion_carrito.py`**

Automatiza acciones del carrito: cambiar cantidades, actualizar productos o eliminarlos.
Tampoco necesita un usuario logueado.

---

### 📦 **`requirements.txt`**

Incluye todas las dependencias necesarias para ejecutar los módulos Selenium.

---

## ⚙️ **Instalación de dependencias**

Ejecuta en la terminal dentro de la carpeta del proyecto:

```bash
pip install -r requirements.txt
```

---

## ▶️ **Cómo ejecutar los scripts**

Puedes ejecutar cualquiera de estos comandos según el módulo que quieras probar:

```bash
python inicio_sesion.py
python registro_usuario.py
python compras_carrito.py
python modificacion_carrito.py
```

---

# 📝 **Configuración de datos antes de ejecutar**

🔴 **IMPORTANTE:**
**Debes rellenar todos los campos vacíos (`""`) antes de ejecutar cualquier script.**
Los nombres de los campos NO deben cambiar, solo completa los valores.

---

## 🔐 **1. Configuración para `inicio_sesion.py`**

Este script utiliza dos conjuntos de datos: para registrarse y para iniciar sesión.

---

### ✏️ a) Datos de registro (`register`)

Completa todos los campos vacíos:

```bash
register = [
    ["nombreCompleto", ""],                # Ej: Juan Alberto Pinto Ibañez
    ["correoElectronico", ""],             # Ej: ju.alpiba@duoc.cl
    ["contrasenaRegistro", ""],            # Ej: Ju@npin34w23
    ["confirmarContrasenaRegistro", ""],   # Ej: Ju@npin34w23
    ["telefono", ""],                      # Ej: 987654321
    ["region", ""],                        # Ej: Metropolitana
    ["comuna", ""]                         # Ej: Santiago
]
```

---

### ✏️ b) Datos de inicio de sesión (`login`)

```bash
login = [
    ["correoAcceso", ""],                  # Ej: ju.alpiba@duoc.cl
    ["contrasenaAcceso", ""]               # Ej: Ju@npin34w23
]
```

---

## 🧑‍💻 **2. Configuración para `registro_usuario.py`**

Rellena los valores vacíos:

```bash
datos = [
    ["nombreCompleto", ""],                # Ej: Juan Alberto Pinto Ibañez       
    ["correoElectronico", ""],             # Ej: ju.alpiba@duoc.cl
    ["contrasenaRegistro", ""],            # Ej: Ju@npin34w23
    ["confirmarContrasenaRegistro", ""],   # Ej: Ju@npin34w23
    ["telefono", ""],                      # Ej: 987654321
    ["region", ""],                        # Ej: Metropolitana
    ["comuna", ""]                         # Ej: Santiago
]
```

---

# 🛒 **3. Configuración para `compras_carrito.py`**

Este módulo utiliza datos del comprador y datos bancarios.
**Todos los valores vacíos deben ser completados antes de ejecutar.**

---

### 👤 a) Datos del comprador

```bash
comprador = [
    ["nombreComprador", ""],               # Ej: Juan Alberto Pinto Ibañez
    ["emailComprador", ""],                # Ej: ju.alpiba@duoc.cl
    ["telefonoComprador", ""],             # Ej: 987654321
    ["direccionComprador", ""]             # Ej: 742 Evergreen Terrace, Springfield
]
```

---

### 💳 b) Datos bancarios

```bash
datos_bancarios = [              
    ["numeroTarjeta", ""],                 # Ej: Juan Alberto Pinto Ibañez
    ["fechaVencimiento", ""],              # Ej: 23/3
    ["cvv", ""]                            # Ej: 133
]
```

---
