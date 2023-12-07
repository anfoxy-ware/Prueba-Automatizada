from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

# Configuración del navegador
options = Options()
options.add_argument("ms:edgeOptions={\"binary\":\"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe\"}")
driver = webdriver.Edge(options=options)

# Abrir la página
driver.get("https://es-la.facebook.com/")

# Inicializar archivo de resultados HTML
with open("resultados.html", "w") as resultados_file:
    # Inicio de sesión
    try:
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

        username.clear()
        password.clear()

        username.send_keys("frandydanieldelacruzarias@gmail.com")
        password.send_keys("Frandy2017*")

        # Hacer clic para iniciar sesión
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='login']"))).click()

        # Esperar y verificar resultados
        time.sleep(2)  # Ajusta el tiempo según sea necesario para que se pueda ver el resultado
        assert "Facebook" in driver.title  # Reemplaza con el título real de la página de destino

        # Escribir resultado exitoso en el archivo HTML
        resultados_file.write("<p style='color: green;'>Inicio de sesion exitoso: PASS</p>\n")

    except Exception as e:
        # Capturar errores y escribir en el archivo HTML
        resultados_file.write(f"<p style='color: red;'>Inicio de sesion fallido: FAIL</p>\n<p>Error: {str(e)}</p>\n")

    finally:
        # Capturar capturas de pantalla y almacenar en un directorio
        driver.save_screenshot("screenshot.png")

        # Cerrar el navegador
        driver.quit()
