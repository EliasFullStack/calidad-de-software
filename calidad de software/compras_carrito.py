import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === COLORES PARA CONSOLA ===
class Color:
    VERDE = "\033[92m"
    ROJO = "\033[91m"
    AMARILLO = "\033[93m"
    AZUL = "\033[94m"
    CYAN = "\033[96m"
    NEGRITA = "\033[1m"
    RESET = "\033[0m"

# === FUNCIÓN DE BARRA DE CARGA ===
def barra_carga(texto="Procesando", duracion=2):
    simbolos = ['|', '/', '-', '\\']
    for i in range(duracion * 4):
        sys.stdout.write(f"\r{Color.CYAN}{texto} {simbolos[i % 4]}{Color.RESET}")
        sys.stdout.flush()
        time.sleep(0.25)
    sys.stdout.write(f"\r{Color.VERDE}{texto} ✅{Color.RESET}\n")

# === FUNCIÓN PARA MOSTRAR MENSAJES invalid-feedback ===
def mostrar_errores(driver):
    errores = driver.find_elements(By.CLASS_NAME, "invalid-feedback")
    for error in errores:
        if error.is_displayed() and error.text.strip() != "":
            print(f"{Color.ROJO}❌ Mensaje de error: {error.text}{Color.RESET}")

# === FUNCIÓN PARA LLENAR CAMPOS CON ASSERTS ===
def llenar_campos(driver, lista_campos, tipo="Comprador"):
    print(f"\n{Color.AZUL}=== Llenando datos del {tipo} ==={Color.RESET}\n")

    for i, (campo, valor) in enumerate(lista_campos, start=1):
        try:
            input_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, campo))
            )
            assert input_element is not None, f"Campo {campo} no encontrado"

            input_element.clear()
            input_element.send_keys(valor)

            barra_carga(f"Llenando campo {i}/{len(lista_campos)}: {campo}", 1)
            print(f"{Color.CYAN}✔ Llenado campo '{campo}' con '{valor}'{Color.RESET}")

            mostrar_errores(driver)

        except Exception as e:
            print(f"{Color.ROJO}❌ Error al llenar campo {campo}: {e}{Color.RESET}")

    # Verificación final de errores
    errores_por_campo = []
    for campo, _ in lista_campos:
        input_elem = driver.find_element(By.ID, campo)
        try:
            feedback_elem = input_elem.find_element(
                By.XPATH, "following-sibling::*[contains(@class,'invalid-feedback')]"
            )
            if feedback_elem.is_displayed() and feedback_elem.text.strip():
                errores_por_campo.append((campo, feedback_elem.text.strip()))
        except:
            continue

    assert len(errores_por_campo) == 0, f"Errores detectados en los campos: {errores_por_campo}"
    print(f"\n{Color.VERDE}✅ Sin errores detectados.{Color.RESET}")


# === FUNCIÓN PRINCIPAL ===
def abrir_inventario(url):
    print(f"\n{Color.NEGRITA}{Color.AZUL}=== INICIANDO AUTOMATIZACIÓN ==={Color.RESET}\n")

    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        print(f"{Color.VERDE}✅ Navegador iniciado correctamente.{Color.RESET}\n")
    except Exception as e:
        print(f"{Color.ROJO}❌ Error al iniciar navegador: {e}{Color.RESET}")
        return

    try:
        print(f"{Color.CYAN}Abriendo página: {Color.RESET}{url}")
        driver.get(url)

        barra_carga("Cargando página", 3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        assert "inventario" in driver.current_url.lower(), "No se abrió la página correcta"

        print(f"{Color.VERDE}✅ Página abierta correctamente.{Color.RESET}\n")

        # Paso 1 - Click 4 veces en btnAgregar-4
        boton_agregar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnAgregar-4"))
        )
        assert boton_agregar is not None, "Botón btnAgregar-4 no encontrado"

        print(f"{Color.CYAN}Presionando 'btnAgregar-4' 4 veces...{Color.RESET}")

        for i in range(4):
            boton_agregar.click()
            print(f"{Color.AMARILLO}👉 Clic número {i+1}{Color.RESET}")
            time.sleep(0.6)

        print(f"{Color.VERDE}✅ Botón 'btnAgregar-4' presionado 4 veces.{Color.RESET}\n")

        # Paso 2 - Click en btnAnadirCarrito-4
        boton_anadir = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnAnadirCarrito-4"))
        )
        assert boton_anadir is not None, "Botón btnAnadirCarrito-4 no encontrado"

        boton_anadir.click()
        print(f"{Color.VERDE}✔ Botón 'btnAnadirCarrito-4' presionado.{Color.RESET}\n")

        # Alerta si existe
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            print(f"{Color.AMARILLO}⚠️ Alerta detectada: {alert.text}{Color.RESET}")
            alert.accept()
            print(f"{Color.VERDE}✔ Alerta aceptada.{Color.RESET}")
        except:
            print(f"{Color.AMARILLO}ℹ️ No apareció alerta.{Color.RESET}")

        # Paso 3 - Click en Mi Carrito
        boton_carrito = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[normalize-space(text())='Mi carrito']"))
        )
        assert boton_carrito is not None, "Botón 'Mi Carrito' no encontrado"

        driver.execute_script("arguments[0].scrollIntoView(true);", boton_carrito)
        boton_carrito.click()
        print(f"{Color.VERDE}✔ 'Mi Carrito' abierto.{Color.RESET}\n")

        # Paso 4 - Datos comprador
        comprador = [
            ["nombreComprador", ""],                # Ej: Juan Alberto pinto Ibañez  
            ["emailComprador", ""],                 # Ej: ju.alpiba@duoc.cl
            ["telefonoComprador", ""],              # Ej: J987654321
            ["direccionComprador", ""]              # Ej: Av. Siempre Viva #641
        ]
        llenar_campos(driver, comprador, "Comprador")

        # Paso 5 - Datos bancarios
        datos_bancarios = [
            ["numeroTarjeta", ""],                  # Ej: 5432 9876 4567 1234
            ["fechaVencimiento", ""],               # Ej: 23/7
            ["cvv", ""]                             # Ej: 133
        ]
        
        llenar_campos(driver, datos_bancarios, "Bancarios")

        # Paso 6 - Confirmar pago
        boton_confirmar_pago = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnConfirmarPago"))
        )
        assert boton_confirmar_pago is not None, "Botón Confirmar Pago no encontrado"

        driver.execute_script("arguments[0].scrollIntoView(true);", boton_confirmar_pago)
        boton_confirmar_pago.click()
        barra_carga("Procesando pago", 2)

        print(f"{Color.VERDE}💳 Pago confirmado correctamente.{Color.RESET}\n")

        
        # Detectar alerta después de añadir producto
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            print(f"{Color.AMARILLO}⚠️ Alerta detectada: {alert.text}{Color.RESET}")
            alert.accept()
            print(f"{Color.VERDE}✔ Alerta aceptada correctamente.{Color.RESET}\n")
        except:
            print(f"{Color.AMARILLO}ℹ️ No apareció alerta al añadir producto.{Color.RESET}\n")




        print(f"{Color.AMARILLO}Esperando 3 segundos antes de cerrar...{Color.RESET}")
        time.sleep(3)

    except AssertionError as error:
        print(f"{Color.ROJO}❌ ASSERT FALLÓ: {error}{Color.RESET}")
    except Exception as e:
        print(f"{Color.ROJO}❌ Error inesperado: {e}{Color.RESET}")

    finally:
        try:
            driver.quit()
            print(f"{Color.VERDE}🚀 Proceso finalizado con éxito.{Color.RESET}")
        except:
            print(f"{Color.ROJO}❌ Error al cerrar navegador.{Color.RESET}")


# === URL Y EJECUCIÓN ===
url = "https://makasuim.github.io/inventario.html"
abrir_inventario(url)
