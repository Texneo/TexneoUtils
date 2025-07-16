from botcity.web.browsers.edge import default_options
from botcity.web import Browser
from time import sleep
import os, time

from selenium.webdriver import EdgeOptions  # ✅ VERSÃO ANTIGA!
from selenium.webdriver.edge.service import Service as EdgeService
from selenium import webdriver

def colocar_em_primeiro_plano(dbot):
    """
    Coloca aplicação do Edge em primeiro plano.
    """
    dbot.connect_to_app(class_name='Chrome_WidgetWin_1', found_index=0)
    janela_edge = dbot.app.top_window()
    janela_edge.set_focus()

def configurar(wbot):
    """
    Prepara EDGE para a execução padrão usando driver fixo.
    """

    diretorio_temp = os.path.join(os.getcwd(), "temp")

    while True:
        try:
            if not os.path.exists(diretorio_temp):
                os.makedirs(diretorio_temp)

            while not os.path.exists(diretorio_temp):
                time.sleep(0.5)
            break
        except:
            pass

    # Configura opções do Edge (API ANTIGA com add_argument)
    def_options = EdgeOptions()
    def_options.add_argument("--start-maximized")
    def_options.add_argument("--remote-debugging-port=9222")
    def_options.add_argument("--inprivate")
    def_options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    def_options.add_experimental_option('useAutomationExtension', False)
    def_options.add_experimental_option('prefs', {
        'browser': {
            'show_hub_popup_on_download_start': False
        }
    })

    # Caminho fixo para o EdgeDriver
    driver_path = r"C:\Users\bot-python-01\Desktop\edgedriver_win64\msedgedriver.exe"
    wbot.driver_path = driver_path
    wbot.options = def_options
    wbot.browser = "EDGE"

    # Se quiser inicializar diretamente:
    # wbot.driver = webdriver.Edge(service=EdgeService(driver_path), options=def_options)
