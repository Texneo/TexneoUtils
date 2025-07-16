from botcity.web.browsers.edge import default_options
from botcity.web import Browser
from time import sleep
import os, time, traceback

from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver

def colocar_em_primeiro_plano(dbot):
    """
    Coloca aplicação do Edge em primeiro plano.
    """
    dbot.connect_to_app(class_name='Chrome_WidgetWin_1', found_index=0)
    janela_edge = dbot.app.top_window()
    janela_edge.set_focus()

def configurar(wbot, url_inicial="www.google.com", max_tentativas=3, espera=5):
    """
    Inicializa o Edge em modo privado usando apenas capabilities,
    e já navega para a URL especificada.
    """

    diretorio_temp = os.path.join(os.getcwd(), "temp")
    os.makedirs(diretorio_temp, exist_ok=True)

    driver_path = r"C:\Users\bot-python-01\Desktop\edgedriver_win64\msedgedriver.exe"

    capabilities = {
        "browserName": "MicrosoftEdge",
        "platform": "WINDOWS",
        "ms:edgeOptions": {
            "args": [
                "--inprivate",
                "--disable-features=Identity,Sync,Extensions",
                "--disable-identity-provider",
                "--no-first-run",
                "--no-default-browser-check",
                f"--user-data-dir={diretorio_temp}",
                "--remote-debugging-port=9222"
            ]
        }
    }

    for i in range(1, max_tentativas+1):
        try:
            print(f"[{i}/{max_tentativas}] Iniciando EdgeDriver...")
            driver = webdriver.Edge(executable_path=driver_path, capabilities=capabilities)

            # Navega imediatamente para a URL desejada
            print("Navegando para:", url_inicial)
            driver.get(url_inicial)

            # Aguarda um pouco para verificar se carrega
            time.sleep(5)

            wbot.driver_path = driver_path
            wbot.browser = "EDGE"
            wbot.driver = driver

            print("Navegador iniciado e conectado com sucesso!")
            return

        except Exception:
            print(f"Falhou na tentativa {i}:")
            traceback.print_exc()
            try:
                driver.quit()
            except:
                pass
            time.sleep(espera)

    raise RuntimeError(f"⚠Não foi possível iniciar o navegador após {max_tentativas} tentativas.")
