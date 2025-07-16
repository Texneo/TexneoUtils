from botcity.web.browsers.edge import default_options
from botcity.web import Browser, WebBot
from time import sleep
import os, time, traceback

from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver

def colocar_em_primeiro_plano(dbot):
    """
    Coloca aplicação do Edge em primeiro plano.
    """
    dbot.connect_to_app(class_name='Chrome_WidgetWin_1', found_index=0)
    janela_edge = dbot.app.top_window()
    janela_edge.set_focus()

def configurar(wbot, url_inicial="https://www.google.com", max_tentativas=3, espera=5):
    """
    Inicializa o Edge em modo privado usando apenas capabilities,
    e já navega para a URL especificada.
    

    diretorio_temp = os.path.join(os.getcwd(), "temp")
    os.makedirs(diretorio_temp, exist_ok=True)

    driver_path = r"C:\Users\bot-python-01\Desktop\edgedriver_win64\msedgedriver.exe"

    capabilities = {
        "browserName": "MicrosoftEdge",
        "ms:edgeOptions": {
            "args": [
                "--inprivate",
                f"--user-data-dir={diretorio_temp}",
                "--disable-extensions",
                "--disable-sync",
                "--disable-features=msControlled,TranslateUI",
                "--remote-debugging-port=9222",
                "--start-maximized"
            ]
        }
    }

    for i in range(1, max_tentativas+1):
        try:
            print(f"[{i}/{max_tentativas}] Iniciando EdgeDriver...")
            driver = webdriver.Edge(executable_path=driver_path, capabilities=capabilities)

            # Navega imediatamente para a URL desejada
            print("Navegando para:", url_inicial)
            driver.get(url_inicial)

            # Aguarda um pouco para verificar se carrega
            time.sleep(5)

            wbot.driver_path = driver_path
            wbot.browser = "EDGE"
            wbot.driver = driver

            print("Navegador iniciado e conectado com sucesso!")
            return

        except Exception:
            print(f"Falhou na tentativa {i}:")
            traceback.print_exc()
            try:
                driver.quit()
            except:
                pass
            time.sleep(espera)

    raise RuntimeError(f"⚠Não foi possível iniciar o navegador após {max_tentativas} tentativas.") """

    # Instantiate the WebBot
    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    profile_path = "C:\\Users\\bot-python-01\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\"

    # Fetch the default options for my preferred browser
    # Pass in the headless, download_folder_path and user_data_dir
    # to be used when building the default_options
    def_options = default_options(
        headless=bot.headless,
        user_data_dir=profile_path  # Inform the profile path that wants to start the browser
    ) 

    # Update the options to use the customized Options.
    bot.options = def_options
    # Set the WebDriver path
    bot.driver_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\"

    wbot = bot
