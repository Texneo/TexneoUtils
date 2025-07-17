from botcity.web import Browser, WebBot
from time import sleep

import os, shutil, time

def colocar_em_primeiro_plano(dbot):
    """
    Coloca aplicação do Edge em primeiro plano.
    """
    dbot.connect_to_app(class_name='Chrome_WidgetWin_1', found_index=0)
    janela_edge = dbot.app.top_window()
    janela_edge.set_focus()

def configurar(wbot):

    """
    
    Prepara EDGE para a execução padrão.

    ->
    wbot: Instância do web bot ativa.
    
    """

    # Definindo navegador como EDGE
    wbot.browser = Browser.EDGE

    wbot.driver_path = "C:\\Users\\bot-python-01\\Documents\\edgedriver_win64\\msedgedriver.exe"

    wbot.headless = False
