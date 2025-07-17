from botcity.web import Browser, WebBot
from time import sleep
from botcity.web.browsers.edge import default_options

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

    def_options = default_options(
        headless=bot.headless,
        download_folder_path="C:\\Users\\bot-python-01\\Downloads",
        user_data_dir=None,  # Informing None here will generate a temporary directory
        page_load_strategy=PageLoadStrategy.NORMAL
    )

    wbot.options = def_options

    # Definindo navegador como EDGE
    wbot.browser = Browser.EDGE

    wbot.driver_path = "C:\\Driver Edge\\edgedriver_win64\\msedgedriver.exe"

    wbot.headless = False
