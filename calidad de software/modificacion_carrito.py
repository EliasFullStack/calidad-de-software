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

# === BARRA DE CARGA ===
def barra_carga(texto="Procesando", duracion=2):
    simbolos = ['|', '/', '-', '\\']
    for i in range(duracion * 4):
        sys.stdout.write(f"\r{Color.CYAN}{texto} {simbolos[i % 4]}{Color.RESET}")
        sys.stdout.flush()
        time.sleep(0.25)
    sys.stdout.write(f"\r{Color.VERDE}{texto} ✅{Color.RESET}\n")

# === FLUJO PRINCIPAL ===
def flujo(url):
    print(f"{Color.AZUL}{Color.NEGRITA}\n=== INICIANDO AUTOMATIZACIÓN ==={Color.RESET}")

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # === 1. ABRIR PÁGINA ===
        print(f"{Color.CYAN}Abriendo página...{Color.RESET}")
        driver.get(url)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        barra_carga("Cargando inventario", 2)

        # === 2. SELECCIONAR PRODUCTO 5 VECES ===
        print(f"{Color.AZUL}\n=== Seleccionando producto 5 veces ==={Color.RESET}")

        btn_agregar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnAgregar-4"))
        )

        for i in range(5):
            btn_agregar.click()
            print(f"{Color.AMARILLO}✔ Selección #{i+1}{Color.RESET}")
            time.sleep(0.5)

        # === 3. AGREGAR AL CARRITO ===
        print(f"{Color.AZUL}\n=== Agregando al carrito ==={Color.RESET}")

        btn_anadir = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnAnadirCarrito-4"))
        )
        btn_anadir.click()
        barra_carga("Añadiendo al carrito", 2)

        # Si aparece alerta, la cierra
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            print(f"{Color.AMARILLO}⚠️ Alerta detectada: {alert.text}{Color.RESET}")
            alert.accept()
        except:
            pass

        # === 4. IR A MI CARRITO ===
        print(f"{Color.AZUL}\n=== Abriendo Mi Carrito ==={Color.RESET}")

        btn_carrito = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[normalize-space(text())='Mi carrito']"))
        )
        btn_carrito.click()
        barra_carga("Entrando a Mi Carrito", 2)

        # === 5. DESELECCIONAR 2 VECES (BOTÓN CLASS: btn-restar) ===
        print(f"{Color.AZUL}\n=== Deseleccionando producto 2 veces ==={Color.RESET}")

        for i in range(2):
            btn_restar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "btn-restar"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", btn_restar)
            btn_restar.click()
            print(f"{Color.AMARILLO}✔ Deselección #{i+1}{Color.RESET}")
            time.sleep(0.5)

        print(f"{Color.VERDE}\n🎉 Flujo ejecutado correctamente.{Color.RESET}")

        time.sleep(2)

    finally:
        driver.quit()
        print(f"{Color.VERDE}🚀 Navegador cerrado.{Color.RESET}")


# === EJECUTAR FLUJO ===
flujo("https://makasuim.github.io/inventario.html")
