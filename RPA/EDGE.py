from botcity.web.browsers.edge import default_options
from botcity.web import Browser
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
from selenium.webdriver.edge.options import Options as EdgeOptions
import os, time

# Monkey‑patch das URLs para EdgeDriver
EdgeChromiumDriverManager._base_url = "https://msedgedriver.microsoft.com"
EdgeChromiumDriverManager._latest_release_url = EdgeChromiumDriverManager._base_url + "/LATEST_RELEASE"

def colocar_em_primeiro_plano(dbot):
    """
    Coloca aplicação do Edge em primeiro plano.

    -> dbot: Instancia do Desktop Bot ativa.
    """
    dbot.connect_to_app(class_name='Chrome_WidgetWin_1', found_index=0)
    janela_edge = dbot.app.top_window()
    janela_edge.set_focus()


def configurar(wbot):
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

    def_options = default_options()
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

    wbot.options = def_options

    # Usa driver manager com URL corrigida
    wbot.driver_path = EdgeChromiumDriverManager().install()

    sleep(5)
    wbot.browser = Browser.EDGE
