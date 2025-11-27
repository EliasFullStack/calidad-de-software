# === IMPORTACIONES ===
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# === CLASE DE COLORES PARA CONSOLA ===
class Color:
    VERDE = "\033[92m"
    ROJO = "\033[91m"
    AMARILLO = "\033[93m"
    AZUL = "\033[94m"
    CYAN = "\033[96m"
    NEGRITA = "\033[1m"
    RESET = "\033[0m"

# === BARRA DE CARGA (estética) ===
def barra_carga(texto="Cargando", duracion=2):
    simbolos = ['|', '/', '-', '\\']
    for i in range(duracion * 4):
        sys.stdout.write(f"\r{Color.CYAN}{texto} {simbolos[i % 4]}{Color.RESET}")
        sys.stdout.flush()
        time.sleep(0.25)
    sys.stdout.write(f"\r{Color.VERDE}{texto} ✅{Color.RESET}\n")

# === FUNCIONES AUXILIARES DE LECTURA/ESPERA ===
def esperar_presencia(driver, by, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))

def esperar_visible(driver, by, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))

def leer_valor_campo(element):
    """
    Devuelve el 'valor visible' real de un campo:
    - select: texto de la opción seleccionada
    - checkbox/radio: 'checked' -> True/False
    - input (text/password/email/number): value attribute
    """
    tag = element.tag_name.lower()
    tipo = (element.get_attribute("type") or "").lower()

    if tag == "select":
        try:
            sel = Select(element)
            return sel.first_selected_option.text.strip()
        except Exception:
            # fallback: value attr
            return (element.get_attribute("value") or "").strip()
    if tipo in ("checkbox", "radio"):
        checked = element.get_attribute("checked")
        return True if checked in ("true", "checked", True) else False
    # default para inputs y textarea
    return (element.get_attribute("value") or "").strip()

# === FUNCIÓN PRINCIPAL ===
def llenar_formulario(url):
    print(f"\n{Color.NEGRITA}{Color.AZUL}🚀 INICIANDO NAVEGADOR...{Color.RESET}")
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(url)
        print(f"🌐 Página abierta: {Color.CYAN}{url}{Color.RESET}\n")
        barra_carga("Preparando entorno", 1)

        # === DATOS DEL FORMULARIO ===
        # Ajusta IDs/valores según lo necesario
        datos = [
            ("nombreCompleto", ""),
            ("correoElectronico", ""),
            ("contrasenaRegistro", ""),
            ("confirmarContrasenaRegistro", ""),
            ("telefono", ""),
            ("region", ""),  #EJ: Metropolitana
            ("comuna", "")   #EJ: Santiago
        ]

        # === 1) Verificar existencia de campos con espera ===
        elementos = {}
        for campo, valor in datos:
            try:
                elem = esperar_presencia(driver, By.ID, campo, timeout=8)
                elementos[campo] = elem
            except Exception as e:
                raise AssertionError(f"No se encontró el campo con id='{campo}' en la página.") from e

        print(f"{Color.NEGRITA}📝 TODOS LOS CAMPOS REQUERIDOS EXISTEN ✔{Color.RESET}")

        # === 2) Llenado de campos y comprobación inmediata ===
        for campo, valor in datos:
            elem = elementos[campo]
            tag = elem.tag_name.lower()
            tipo = (elem.get_attribute("type") or "").lower()

            print(f"   ✏️ {Color.AMARILLO}{campo}{Color.RESET} → {valor}")

            # Si es select, tratarlo como Select
            if tag == "select":
                try:
                    sel = Select(elem)
                    # intentar seleccionar por visible text; si falla, intentar por value
                    try:
                        sel.select_by_visible_text(valor)
                    except Exception:
                        sel.select_by_value(valor)
                except Exception as e:
                    raise AssertionError(f"Campo '{campo}' parece ser un <select> pero no se pudo seleccionar '{valor}': {e}") from e
            elif tipo in ("checkbox", "radio"):
                # Para checkbox/radio: marcar si valor es truthy
                should_check = bool(valor)
                is_checked = elem.get_attribute("checked") in ("true", "checked", True)
                if should_check and not is_checked:
                    elem.click()
                elif not should_check and is_checked:
                    elem.click()
            else:
                # inputs y textarea
                try:
                    elem.clear()
                except Exception:
                    pass
                elem.send_keys(valor)

            # pequeña espera para que el DOM se actualice
            time.sleep(0.25)

            # === ASSERT mejorado: comprobar que el campo ahora contiene lo esperado ===
            valor_leido = leer_valor_campo(elem)

            # Normalizamos para comparar (quita espacios extremos y baja a minúsculas para compare textuales)
            if isinstance(valor_leido, bool):
                # para checkbox/radio
                expected_bool = bool(valor)
                assert valor_leido == expected_bool, (
                    f"El campo '{campo}' (checkbox/radio) tiene estado {valor_leido} pero se esperaba {expected_bool}."
                )
            else:
                # comparar strings, relajar igualdad si puede haber diferencias en mayúsculas/minúsculas
                if valor_leido != valor:
                    # permitir coincidencia por case-insensitive o trimmed
                    if valor_leido.lower() != valor.lower():
                        raise AssertionError(
                            f"El campo '{campo}' contiene '{valor_leido}' pero se esperaba '{valor}'."
                        )
            # feedback
            print(f"      {Color.VERDE}✔ Valor verificado: {valor_leido}{Color.RESET}")

        # === 3) Verificar y hacer clic en boton 'eliminar mascota' ===
        try:
            btn_eliminar_mascota = esperar_visible(driver, By.XPATH, "//button[normalize-space()='Eliminar Mascota' or contains(.,'Eliminar Mascota')]", timeout=8)
        except Exception:
            raise AssertionError("Botón 'Eliminar Mascota' no encontrado o no visible en la página.")

        assert btn_eliminar_mascota.is_enabled(), "El botón 'Eliminar Mascota' existe pero está deshabilitado."

        print(f"\n🔎 {Color.NEGRITA}Botón 'Eliminar Mascota' encontrado y habilitado.{Color.RESET}")
        btn_eliminar_mascota.click()
        barra_carga("Enviando datos", 2)
        time.sleep(1)
        
        # === 3) Verificar y hacer clic en boton 'Registrarse' ===
        try:
            btn_register = esperar_visible(driver, By.XPATH, "//button[normalize-space()='Registrarse' or contains(.,'Registrarse')]", timeout=8)
        except Exception:
            raise AssertionError("Botón 'Registrarse' no encontrado o no visible en la página.")

        assert btn_register.is_enabled(), "El botón 'Registrarse' existe pero está deshabilitado."

        print(f"\n🔎 {Color.NEGRITA}Botón 'Registrarse' encontrado y habilitado.{Color.RESET}")
        btn_register.click()
        barra_carga("Enviando datos", 2)
        time.sleep(1)

        # === 4) Comprobar errores visibles por campo (feedback) ===
        errores_por_campo = []
        for campo, _ in datos:
            # intentamos localizar un elemento de feedback relativo al input
            try:
                input_elem = elementos[campo]
                # Buscar cualquier elemento siguiente con clase que contenga 'invalid' o 'error' o 'invalid-feedback'
                # usamos find_elements para no lanzar excepción
                posibles = input_elem.find_elements(By.XPATH, "following-sibling::*[contains(@class,'invalid') or contains(@class,'error') or contains(@class,'invalid-feedback')]")
                for p in posibles:
                    text = (p.text or "").strip()
                    if text:
                        errores_por_campo.append((campo, text))
            except Exception:
                # no crítico, seguimos
                continue

        # ASSERT: no errores visibles
        assert len(errores_por_campo) == 0, "Se detectaron mensajes de error en el formulario: " + "; ".join([f"{c} -> {m}" for c, m in errores_por_campo])

        print(f"\n{Color.VERDE}✅ No se detectaron errores visibles en los campos.{Color.RESET}")

        # === 5) Mensaje de registro final (opcional) ===
        try:
            mensaje_elem = driver.find_element(By.ID, "mensajeRegistro")
            if mensaje_elem.is_displayed():
                mensaje_texto = (mensaje_elem.text or "").strip()
                print(f"\n💬 Mensaje de registro: {Color.CYAN}{mensaje_texto}{Color.RESET}")
                assert mensaje_texto != "", "El elemento 'mensajeRegistro' está visible pero su texto está vacío."
        except Exception:
            # si no existe el mensaje, no es obligatorio; solo mostramos aviso
            print(f"{Color.AMARILLO}⚠️ No se encontró elemento 'mensajeRegistro' (esto puede ser válido según la implementación).{Color.RESET}")

        print(f"\n🎉 {Color.NEGRITA}{Color.VERDE}FORMULARIO COMPLETADO Y VALIDADO ✔{Color.RESET}\n")

    except AssertionError as ae:
        print(f"\n{Color.ROJO}ASSERTION FAILED: {ae}{Color.RESET}\n")
    except Exception as e:
        print(f"\n{Color.ROJO}ERROR INESPERADO: {e}{Color.RESET}\n")
    finally:
        driver.quit()
        print(f"{Color.AMARILLO}🛑 Navegador cerrado.{Color.RESET}")

# === EJECUCIÓN ===
if __name__ == "__main__":
    llenar_formulario("https://makasuim.github.io/registro.html")

