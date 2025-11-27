# 🌐 **Proyecto – Calidad de Software (DUOC UC)** Este repositorio corresponde al ramo **Calidad de Software** del Instituto Profesional **DUOC UC**, donde se trabajan prácticas de: ✔️ Validación ✔️ Automatización ✔️ Aseguramiento de Calidad Todo mediante la ejecución de **pruebas automatizadas con Selenium** para evaluar el correcto funcionamiento de una aplicación web. El proyecto está compuesto por **cuatro módulos de automatización**, cada uno orientado a un flujo clave: inicio de sesión, registro, compras y gestión del carrito. --- ## 📁 **Estructura del Repositorio** ### 🔐 **inicio_sesion.py** Automatiza el flujo completo de **registro + inicio de sesión**. El script registra primero al usuario y luego utiliza esos datos almacenados para validar el acceso. --- ### 🧑‍💻 **registro_usuario.py** Simula el registro de un nuevo usuario, validando campos, mensajes del sistema y almacenamiento local de datos. --- ### 🛒 **compras_carrito.py** Simula la **selección y compra** de productos. Este flujo **no requiere inicio de sesión**, por lo que puede ejecutarse de forma independiente. --- ### 🛍️ **modificacion_carrito.py** Automatiza acciones dentro del carrito: cambiar cantidad, actualizar productos o eliminarlos. Tampoco depende de estar autenticado. --- ### 📦 **requirements.txt** Incluye todas las dependencias necesarias para ejecutar los módulos de automatización. --- ## ⚙️ **Instalación de dependencias** Ejecuta en la terminal dentro de la carpeta del proyecto:
bash
pip install -r requirements.txt
--- ## ▶️ **Cómo ejecutar los scripts** Usa cualquiera de los siguientes comandos según el módulo que quieras probar:
bash
python inicio_sesion.py
bash
python registro_usuario.py
bash
python compras_carrito.py
bash
python modificacion_carrito.py
--- # 📝 **Configuración de datos antes de ejecutar** Algunos scripts requieren actualizar valores dentro de arreglos. A continuación, se detalla qué debes modificar según cada archivo. --- ## 🔐 **1. Configuración para inicio_sesion.py** Este script requiere completar **datos de registro** y **datos de inicio de sesión**. ### ✏️ **a) Datos de registro** (register)
bash
register = [
    ["nombreCompleto", ""],                # Ej: Juan Alberto pinto Ibañez
    ["correoElectronico", ""],             # Ej: ju.alpiba@duoc.cl
    ["contrasenaRegistro", ""],            # Ej: Ju@npin34w23
    ["confirmarContrasenaRegistro", ""],   # Ej: Ju@npin34w23
    ["telefono", "987654321"],             # Ej: 987654321
    ["region", ""],                        # Ej: Metropolitana
    ["comuna", ""]                         # Ej: Santiago
]
--- ### ✏️ **b) Datos de inicio de sesión** (login)
bash
login = [
    ["correoAcceso", ""],                  # Ej: ju.alpiba@duoc.cl
    ["contrasenaAcceso", ""]               # Ej: Ju@npin34w23
]
--- ## 🧑‍💻 **2. Configuración para registro_usuario.py** Debes **reemplazar solo los valores vacíos** en la segunda columna:
bash
datos = [
    ["nombreCompleto", ""],                # Ej: Juan Alberto pinto Ibañez     
    ["correoElectronico", ""],             # Ej: ju.alpiba@duoc.cl
    ["contrasenaRegistro", ""],            # Ej: Ju@npin34w23
    ["confirmarContrasenaRegistro", ""],   # Ej: Ju@npin34w23
    ["telefono", ""],                      # Ej: 987654321
    ["region", ""],                        # Ej: Metropolitana
    ["comuna", ""]                         # Ej: Santiago
]
--- # 🛒 **3. Configuración para compras (compras_carrito.py)** Este módulo requiere datos del **comprador** y de **pago**. ### 👤 **a) Datos del comprador**
bash
comprador = [
    ["nombreComprador", ""],                # Ej: Juan Alberto pinto Ibañez  
    ["emailComprador", ""],                 # Ej: ju.alpiba@duoc.cl
    ["telefonoComprador", ""],              # Ej: J987654321
    ["direccionComprador", ""]              # Ej: Av. Siempre Viva #641
]
--- ### 💳 **b) Datos bancarios**
bash
datos_bancarios = [
    ["numeroTarjeta", ""],                  # Ej: 5432 9876 4567 1234
    ["fechaVencimiento", ""],               # Ej: 23/7
    ["cvv", ""]                             # Ej: 133
]
---
