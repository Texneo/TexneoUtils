from botcity.web.browsers.edge import default_options
from botcity.web import Browser
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
import os, shutil, time

def colocar_em_primeiro_plano(dbot):

    """
    
    Coloca aplicação do Edge em primeiro plano.

    ->
    dbot: Instancia do Desktop Bot ativa.
    
    """
    
    dbot.connect_to_app(class_name = 'Chrome_WidgetWin_1', found_index=0)
    janela_edge = dbot.app.top_window()
    janela_edge.set_focus()

def configurar(wbot):
    """
    Prepara EDGE para a execução padrão.

    -> wbot: Instância do web bot ativa.
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

    # Atribui as opções ao bot
    wbot.options = def_options

    # Define caminho do driver com nova URL já usada automaticamente na nova versão do webdriver-manager
    wbot.driver_path = EdgeChromiumDriverManager().install()

    sleep(5)

    # Define navegador como EDGE
    wbot.browser = "EDGE"
