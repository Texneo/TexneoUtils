from botcity.web.browsers.edge import default_options
from botcity.web import Browser
from webdriver_manager.microsoft import EdgeChromiumDriverManager
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

    diretorio_temp = os.path.join(os.getcwd(), f"temp")

    while True:
        try:
            if os.path.exists(diretorio_temp):
                pass
            else:
                os.makedirs(diretorio_temp)
        
            while not os.path.exists(diretorio_temp):
                time.sleep(0.5)
            break
        except:
            pass

    def_options = default_options()
    def_options.add_argument("--start-maximized")
    def_options.add_argument("--remote-debugging-port=9222")
    def_options.add_argument("--inprivate")
    def_options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    def_options.add_experimental_option('useAutomationExtension', False)
    def_options.add_experimental_option('prefs', {'browser':{'show_hub_popup_on_download_start': False}})
    wbot.options = def_options

    # Definindo caminho do Driver
    manager = EdgeChromiumDriverManager()
    wbot.driver_path = manager.install()

    sleep(5)

    # Definindo navegador como EDGE
    wbot.browser = Browser.EDGE
