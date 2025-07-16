from botcity.web.browsers.edge import default_options
from botcity.web import Browser
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.core.download_manager import WDMDownloadManager
from webdriver_manager.core.driver_cache import DriverCache
from webdriver_manager.core.logger import log
from webdriver_manager.core.os_manager import OperationSystemManager
from webdriver_manager.core.utils import get_browser_version_from_os

from selenium.webdriver.edge.options import Options as EdgeOptions
from time import sleep
import os, time


class CustomEdgeDriverManager(EdgeChromiumDriverManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver_cache = DriverCache(valid_range=1)
        self.download_manager = WDMDownloadManager(
            root_dir=self.driver_cache._root_dir,
            os_manager=OperationSystemManager(),
            ssl_verify=True
        )
        # Forçando nova URL da Microsoft
        self._base_url = "https://msedgedriver.microsoft.com"
        self._latest_release_url = self._base_url + "/LATEST_RELEASE"


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

    # Diretório temporário
    diretorio_temp = os.path.join(os.getcwd(), "temp")

    while True:
        try:
            if not os.path.exists(diretorio_temp):
                os.makedirs(diretorio_temp)

            while not os.path.exists(diretorio_temp):
                time.sleep(0.5)
            break
        except Exception:
            pass

    # Configurações do Edge via BotCity
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

    # Usa o driver manager com URL hardcoded corrigida
    driver_manager = CustomEdgeDriverManager()
    wbot.driver_path = driver_manager.install()

    sleep(5)

    # Define navegador como EDGE
    wbot.browser = Browser.EDGE
