from botcity.web.browsers.edge import default_options
from botcity.web import Browser
from time import sleep
import os, time

from webdriver_manager.core.driver import Driver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions

# 🔧 Subclasse do Driver para forçar URL nova
class CustomEdgeDriver(Driver):
    def __init__(self, name, version, os_type):
        super().__init__(name, version, os_type)
    
    def get_latest_release_url(self):
        # Força o novo domínio
        return f"https://msedgedriver.microsoft.com/LATEST_RELEASE"

    def get_driver_url(self, version):
        # Força o novo domínio
        base_url = "https://msedgedriver.microsoft.com"
        platform = "WIN64" if "64" in self.os_type else "WIN32"
        return f"{base_url}/edgedriver/{version}/edgedriver_{platform}.zip"

# Subclasse do Manager que usa o CustomEdgeDriver
class CustomEdgeDriverManager(EdgeChromiumDriverManager):
    def get_driver(self):
        return CustomEdgeDriver(name="edgedriver", version=self.driver_version, os_type=self.os_type)


def colocar_em_primeiro_plano(dbot):
    """
    Coloca aplicação do Edge em primeiro plano.

    -> dbot: Instancia do Desktop Bot ativa.
    """
    dbot.connect_to_app(class_name='Chrome_WidgetWin_1', found_index=0)
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

    # Usa o CustomEdgeDriverManager com URL corrigida
    wbot.driver_path = CustomEdgeDriverManager().install()

    sleep(5)
    wbot.browser = Browser.EDGE
