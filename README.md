# 📌 Proyecto – Calidad de Software (DUOC UC)

Este repositorio corresponde al ramo Calidad de Software del Instituto Profesional DUOC UC, donde se desarrollan actividades orientadas a la validación, automatización y aseguramiento de la calidad en aplicaciones web mediante el uso de Selenium.
Su propósito es aplicar técnicas de pruebas automatizadas para evaluar el correcto funcionamiento de distintos flujos dentro de una aplicación.

El repositorio está compuesto por cuatro módulos de automatización, cada uno centrado en una funcionalidad clave de una aplicación web: inicio de sesión, registro de usuario, proceso de compra y modificación del carrito.

## 🧭 Contenido del repositorio

**`inicio_sesion.py` →** Este script incluye tanto el formulario de registro como el proceso de inicio de sesión. Su función es permitir que el usuario primero complete el registro y, una vez almacenados esos datos en la base local, pueda iniciar sesión correctamente. Si el usuario no se registra, el sistema no tendría datos para validar el correo o la contraseña, por lo que el propio código implementa este flujo: **primero registrar y luego iniciar sesión**.

**`registro_usuario.py` →** Ejecuta el flujo completo de registro de un nuevo usuario, gestionando el ingreso de datos, las validaciones de cada campo y los mensajes que entrega el sistema durante el proceso. Su función es almacenar correctamente la información del usuario en la base local para que posteriormente pueda utilizar las demás funcionalidades del proyecto.


**`compras_carrito.py` →** Simula la selección y el agregado de productos al carrito, además de avanzar en el flujo de compra. Este script funciona de manera independiente al inicio de sesión, por lo que puede ejecutarse sin que el usuario esté autenticado.

**`modificacion_carrito.py` →** Automatiza acciones dentro del carrito, como modificar cantidades, actualizar productos o eliminarlos. Al igual que el flujo de compra, este proceso no depende de que el usuario haya iniciado sesión.


**`requirements.txt` →** Archivo que contiene todas las dependencias necesarias para ejecutar los scripts de automatización.


## ⚙️ Instalación de dependencias (requirements.txt)

Para instalar las librerías necesarias para ejecutar los scripts del proyecto, debes usar el archivo requirements.txt.
En la terminal, ejecuta el siguiente comando dentro de la carpeta del repositorio:
```bash
pip install -r requirements.txt
```

## ▶️ Ejecución de los scripts

Para ejecutar cada uno de los módulos de automatización, utiliza los siguientes comandos en la terminal:

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
Aquí tienes una versión clara y breve:

---

Para ejecutar el script **`registro_usuario.py`**, debes **reemplazar los valores vacíos** en la segunda columna de cada campo. Los nombres de los campos deben mantenerse sin cambios.

```bash
datos = [
    ["nombreCompleto", ""],
    ["correoElectronico", ""],
    ["contrasenaRegistro", ""],
    ["confirmarContrasenaRegistro", ""],
    ["telefono", ""],
    ["region", ""],    # Ej: Metropolitana
    ["comuna", ""]     # Ej: Santiago
]
```

---

