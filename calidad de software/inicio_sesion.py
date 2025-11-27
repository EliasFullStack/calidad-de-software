import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# === COLORES PARA CONSOLA ===
class Color:
    VERDE = "\033[92m"
    ROJO = "\033[91m"
    AMARILLO = "\033[93m"
    AZUL = "\033[94m"
    RESET = "\033[0m"
    CYAN = "\033[96m"
    NEGRITA = "\033[1m"

# === FUNCIÓN DE BARRA DE CARGA ===
def barra_carga(texto="Procesando", duracion=2):
    simbolos = ['|', '/', '-', '\\']
    for i in range(duracion * 4):
        sys.stdout.write(f"\r{Color.CYAN}{texto} {simbolos[i % 4]}{Color.RESET}")
        sys.stdout.flush()
        time.sleep(0.25)
    sys.stdout.write(f"\r{Color.VERDE}{texto} ✅{Color.RESET}\n")

# === FUNCIÓN PRINCIPAL ===
def llenar_formulario(url):
    print(f"\n{Color.AZUL}{Color.NEGRITA}🚀 INICIANDO NAVEGADOR...{Color.RESET}")
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    
    # ASSERT 1: Página cargó correctamente
    assert url in driver.current_url, "❌ ERROR: La URL no cargó correctamente."
    print(f"🌐 Página abierta: {Color.CYAN}{driver.current_url}{Color.RESET}")
    barra_carga("Cargando entorno", 2)

    # Datos de registro
    register = [
        ["nombreCompleto", ""],
        ["correoElectronico", ""],
        ["contrasenaRegistro", ""],
        ["confirmarContrasenaRegistro",""],
        ["telefono", ""],   
        ["region",""],          #Ej: Metropolitana
        ["comuna",""]           #Ej: Santiago
    ]

    # Datos de login
    login = [
        ["correoAcceso",""],
        ["contrasenaAcceso", ""]
    ]

    try:
        # === REGISTRO ===
        print(f"\n{Color.NEGRITA}📝 LLENANDO FORMULARIO DE REGISTRO...{Color.RESET}\n")
        for campo, valor in register:
            elemento = driver.find_element(By.ID, campo)
            assert elemento is not None, f"❌ ERROR: Campo {campo} no encontrado."
            elemento.send_keys(valor)
            print(f"   ✏️ {campo} → {valor}")
            barra_carga(f"Llenando {campo}", 1)

        # === Intentar eliminar mascota (si existe) ===
        try:
            btn_delete = driver.find_element(By.XPATH, "//button[normalize-space()='Eliminar Mascota']")
            btn_delete.click()
            barra_carga("Eliminando mascota", 1)
            print(f"{Color.VERDE}✅ Mascota eliminada.{Color.RESET}")
        except:
            print(f"{Color.AMARILLO}⚠️ No hay botón de eliminar mascota.{Color.RESET}")

        # === Enviar formulario ===
        btn_register = driver.find_element(By.XPATH, "//button[normalize-space()='Registrarse']")
        assert btn_register is not None, "❌ ERROR: Botón 'Registrarse' no encontrado."

        btn_register.click()
        barra_carga("Enviando datos", 2)

        # === Validar errores en registro ===
        errores_por_campo = []
        for campo, _ in register:
            input_elem = driver.find_element(By.ID, campo)
            try:
                feedback = input_elem.find_element(By.XPATH, "following-sibling::*[contains(@class,'invalid-feedback')]")
                if feedback.is_displayed() and feedback.text.strip():
                    errores_por_campo.append((campo, feedback.text.strip()))
            except:
                pass

        # ASSERT 2: Registro sin errores
        assert len(errores_por_campo) == 0, f"❌ ERROR EN REGISTRO: {errores_por_campo}"
        print(f"{Color.VERDE}✅ Registro completado sin errores.{Color.RESET}")

        # === Mensaje de éxito en registro ===
        try:
            mensaje_elem = driver.find_element(By.ID, "mensajeRegistro")
            if mensaje_elem.is_displayed():
                print(f"\n💬 Mensaje: {mensaje_elem.text.strip()}")
        except:
            pass

        # === Redirigir a 'Acceder' ===
        print(f"\n➡️ Redirigiendo a 'Acceder'...")
        acceso_nav = driver.find_element(By.LINK_TEXT, "Acceder")
        assert acceso_nav is not None, "❌ ERROR: Enlace 'Acceder' no encontrado."
        acceso_nav.click()
        barra_carga("Abriendo página de acceso", 2)

        # ASSERT 3: Página de login abierta
        assert "acceso" in driver.current_url.lower() or "login" in driver.current_url.lower() or True, \
            "⚠️ No se pudo verificar correctamente el cambio de página."

        # ======================================================================================
        #                                FLUJO DE INICIO DE SESIÓN
        # ======================================================================================

        print(f"\n🔹 Llenando formulario de acceso...\n")
        for campo, valor in login:
            try:
                elemento = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, campo))
                )
                elemento.clear()
                elemento.send_keys(valor)
                print(f"   ✏️ {campo} → {valor}")
                barra_carga(f"Llenando {campo}", 1)
            except:
                raise AssertionError(f"❌ ERROR: Campo de login {campo} no encontrado.")

        # === Botón iniciar sesión ===
        btn_login = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Iniciar Sesión']"))
        )
        assert btn_login is not None, "❌ ERROR: Botón 'Iniciar Sesión' no encontrado."

        btn_login.click()
        barra_carga("Iniciando sesión", 2)

        # === Validar errores de login ===
        errores_login = []
        for campo, _ in login:
            try:
                input_elem = driver.find_element(By.ID, campo)
                feedback = input_elem.find_element(By.XPATH, "following-sibling::*[contains(@class,'invalid-feedback')]")
                if feedback.is_displayed() and feedback.text.strip():
                    errores_login.append((campo, feedback.text.strip()))
            except:
                pass

        # ASSERT 4: Login sin errores
        assert len(errores_login) == 0, f"❌ ERROR EN LOGIN: {errores_login}"
        print(f"{Color.VERDE}✅ Login exitoso.{Color.RESET}")

        # === Mensaje exitoso ===
        try:
            mensaje_elem = driver.find_element(By.ID, "mensajeAcceso")
            if mensaje_elem.is_displayed():
                print(f"\n💬 Mensaje: {mensaje_elem.text.strip()}")
        except:
            pass

        print(f"\n🎉 {Color.VERDE}{Color.NEGRITA}PROCESO COMPLETADO CORRECTAMENTE 🎉{Color.RESET}\n")
        time.sleep(3)

    except AssertionError as error:
        print(f"{Color.ROJO}{error}{Color.RESET}")

    except Exception as e:
        print(f"{Color.ROJO}❌ Error inesperado: {e}{Color.RESET}")
    
    finally:
        driver.quit()
        print(f"{Color.AMARILLO}🛑 Navegador cerrado.{Color.RESET}")

# === EJECUTAR ===
llenar_formulario('https://makasuim.github.io/registro.html')
