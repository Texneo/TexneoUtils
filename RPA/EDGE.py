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
    
    driver_path = r"C:\Users\bot-python-01\Desktop\edgedriver_win64\msedgedriver.exe"

    #options = Options()
    #options.use_chromium = True  # necessário para Edge moderno

    # Esses atributos podem não funcionar em versões muito antigas
    #options.add_argument("--start-maximized")
    #options.add_argument("--remote-debugging-port=9222")
    #options.add_argument("--inprivate")

    # No Selenium muito antigo (pré-3.8), apenas isso funciona:
    driver = webdriver.Edge(executable_path=driver_path)

    # Configuração para o wbot
    wbot.driver_path = driver_path
    #wbot.options = options
    wbot.browser = "EDGE"
    wbot.driver = driver
