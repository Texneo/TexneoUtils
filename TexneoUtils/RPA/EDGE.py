from botcity.web.browsers.edge import default_options
from botcity.web import Browser

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

    ->
    wbot: Instância do web bot ativa.
    
    """

    def_options = default_options()
    def_options.add_argument("--remote-debugging-port=9999")
    def_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    def_options.add_experimental_option('prefs', {'browser':{'show_hub_popup_on_download_start': False}})
    wbot.options = def_options

    # Definindo caminho do Driver
    wbot.driver_path = r"C:\Users\bot-python-01\Documents\WebDrivers\msedgedriver.exe"

    # Definindo navegador como EDGE
    wbot.browser = Browser.EDGE