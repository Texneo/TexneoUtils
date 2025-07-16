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

    service = EdgeService(r"C:\Users\bot-python-01\Desktop\edgedriver_win64\msedgedriver.exe")
    options = Options()
    #options.add_argument("--start-maximized")
    #options.add_argument("--remote-debugging-port=9222")
    #options.add_argument("--inprivate")

    driver_path = r"C:\Users\bot-python-01\Desktop\edgedriver_win64\msedgedriver.exe"
    
    driver = webdriver.Edge(executable_path=driver_path, options=options)

    # Caminho fixo para o EdgeDriver
    wbot.driver_path = driver_path
    wbot.options = options
    wbot.browser = "EDGE"
    wbot.driver = webdriver.Edge(options = options)
