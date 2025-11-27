# 🌐 **Proyecto – Calidad de Software (DUOC UC)**

Este repositorio corresponde al ramo **Calidad de Software** del Instituto Profesional **DUOC UC**, donde se trabajan prácticas de:

✔️ Validación
✔️ Automatización
✔️ Aseguramiento de Calidad

Todo mediante la ejecución de **pruebas automatizadas con Selenium** para evaluar el correcto funcionamiento de una aplicación web.

El proyecto está compuesto por **cuatro módulos de automatización**, cada uno orientado a un flujo clave: inicio de sesión, registro, compras y gestión del carrito.

---

## 📁 **Estructura del Repositorio**

### 🔐 **`inicio_sesion.py`**

Automatiza el flujo completo de **registro + inicio de sesión**.
Primero registra al usuario y luego utiliza esos mismos datos almacenados para validar el acceso.

---

### 🧑‍💻 **`registro_usuario.py`**

Simula el registro de un nuevo usuario, validando campos, mensajes del sistema y el guardado de información.

---

### 🛒 **`compras_carrito.py`**

Simula la **selección y compra de productos**.
Este flujo **no requiere autenticación** y puede ejecutarse de forma independiente.

---

### 🛍️ **`modificacion_carrito.py`**

Automatiza acciones dentro del carrito: actualizar cantidades, modificar productos o eliminarlos.
Tampoco depende de un usuario autenticado.

---

### 📦 **`requirements.txt`**

Incluye todas las dependencias necesarias para ejecutar los módulos de automatización.

---

## ⚙️ **Instalación de dependencias**

Ejecuta en la terminal dentro de la carpeta del proyecto:

```bash
pip install -r requirements.txt
```

---

## ▶️ **Cómo ejecutar los scripts**

Usa cualquiera de los siguientes comandos según el módulo que quieras probar:

```bash
python inicio_sesion.py
```
```bash
python registro_usuario.py
```
```bash
python compras_carrito.py
```
```bash
python modificacion_carrito.py
```

---

# 📝 **Configuración de datos antes de ejecutar**

🔴 **IMPORTANTE:**
**Todos los scripts requieren que completes los campos vacíos (`""`) antes de ejecutar.
Debes reemplazar únicamente los valores vacíos, manteniendo los nombres de los campos intactos.**

---

## 🔐 **1. Configuración para `inicio_sesion.py`**

Este script utiliza **dos arreglos de datos**: uno para el registro y otro para el inicio de sesión.

### ✏️ a) Datos de registro (`register`)

Completa los valores vacíos con los datos que quieras usar:

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

Aquí también debes **llenar cada valor vacío** antes de ejecutar:

```bash
datos = [
    ["nombreCompleto", ""],                
    ["correoElectronico", ""],             
    ["contrasenaRegistro", ""],            
    ["confirmarContrasenaRegistro", ""],   
    ["telefono", ""],                      
    ["region", ""],                        
    ["comuna", ""]                         
]
```

---

# 🛒 **3. Configuración para `compras_carrito.py`**

Este módulo utiliza datos del **comprador** y los **datos bancarios**.
✔️ **Debes completar todos los valores vacíos**.

### 👤 a) Datos del comprador

```bash
comprador = [
    ["nombreComprador", ""],               
    ["emailComprador", ""],                
    ["telefonoComprador", ""],             
    ["direccionComprador", ""]
]
```

---

### 💳 b) Datos bancarios

```bash
datos_bancarios = [
    ["numeroTarjeta", ""],
    ["fechaVencimiento", ""],
    ["cvv", ""]
]
```

---
