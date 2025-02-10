from selenium.webdriver.chrome.options import Options
from botcity.web import Browser
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os

def colocar_em_primeiro_plano(dbot):

    """
    
    Coloca aplicação do Edge em primeiro plano.

    ->
    dbot: Instancia do Desktop Bot ativa.
    
    """
    
    dbot.connect_to_app(class_name = 'Chrome_WidgetWin_1', found_index=0)
    janela_edge = dbot.app.top_window()
    janela_edge.set_focus()

def is_browser_session_active(driver):
    try:
        driver.get("https://www.google.com")  # Tenta acessar uma página simples
        return True
    except Exception as e:
        return False

def configurar(wbot):

    """
    
    Prepara EDGE para a execução padrão.

    ->
    wbot: Instância do web bot ativa.
    
    """
    tentativas = 0
    maximo_tentativas = 5
    while tentativas < maximo_tentativas:
        
        try:
            def_options = Options()
            def_options.add_argument("--start-maximized")
            def_options.add_argument("--no-sandbox")
            def_options.add_argument(f"--user-data-dir={create_unique_user_data_dir()}")
            def_options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
            def_options.add_experimental_option('useAutomationExtension', False)
            def_options.add_experimental_option('prefs', {'browser':{'show_hub_popup_on_download_start': False}})
            wbot.options = def_options
        
            # Definindo caminho do Driver
            manager = ChromeDriverManager()
            wbot.driver_path = manager.install()
        
            sleep(5)
        
            # Definindo navegador como EDGE
            wbot.browser = Browser.CHROME

            driver_service = Service(wbot.driver_path)
            wbot.browser = webdriver.Chrome(service=driver_service, options=def_options)
    
            if is_browser_session_active(wbot.browser):
                print("Sessão do navegador CHROME criada com sucesso!")
                return  # Retorna se a sessão estiver ativa
            else:
                raise Exception("Sessão não ativa, tentando novamente...")
        except:

            tentativas+=1
            if tentativas >= maximo_tentativas:
                print("Falha ao criar a sessão após várias tentativas.")
                raise Exception("Não foi possível criar uma sessão do navegador após várias tentativas.")
    
def create_unique_user_data_dir(base_path="C:\\Users\\bot-python-01\\Documents\\EdgeCache"):
    user_data_dir = base_path + "_unique"  # Adiciona sufixo "_unique" para garantir exclusividade
    if not os.path.exists(user_data_dir):
        os.makedirs(user_data_dir)
    return user_data_dir
