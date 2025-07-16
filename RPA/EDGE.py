from botcity.web.browsers.edge import default_options
from botcity.web import Browser
from time import sleep
import os, time

from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from selenium import webdriver

def colocar_em_primeiro_plano(dbot):
    """
    Coloca aplicação do Edge em primeiro plano.
    """
    dbot.connect_to_app(class_name='Chrome_WidgetWin_1', found_index=0)
    janela_edge = dbot.app.top_window()
    janela_edge.set_focus()

def configurar(wbot, max_tentativas=3, espera_entre_tentativas=5):
    driver_path = r"C:\Users\bot-python-01\Desktop\edgedriver_win64\msedgedriver.exe"

    options = Options()
    options.use_chromium = True
    options.add_argument("--start-maximized")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--inprivate")
    options.add_argument(f"user-data-dir={diretorio_temp}")

    tentativa = 0

    while tentativa < max_tentativas:
        try:
            print(f"Tentando iniciar o EdgeDriver (tentativa {tentativa+1}/{max_tentativas})...")

            driver = webdriver.Edge(executable_path=driver_path)

            # Configura o wbot
            wbot.driver_path = driver_path
            #wbot.options = options
            wbot.browser = "EDGE"
            wbot.driver = driver

            print("✅ Navegador iniciado com sucesso.")
            return  # sai da função após sucesso

        except Exception as e:
            print(f"❌ Erro ao iniciar o EdgeDriver: {e}")
            tentativa += 1

            # Tenta encerrar qualquer driver pendente
            try:
                driver.quit()
            except:
                pass

            time.sleep(espera_entre_tentativas)

    raise Exception(f"❌ Não foi possível iniciar o navegador após {max_tentativas} tentativas.")
