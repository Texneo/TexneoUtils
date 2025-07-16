from botcity.web.browsers.edge import default_options
from botcity.web import Browser
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

def configurar(wbot, max_tentativas=3, espera=5):
    diretorio_temp = os.path.join(os.getcwd(), "temp")
    os.makedirs(diretorio_temp, exist_ok=True)

    driver_path = r"C:\Users\bot-python-01\Desktop\edgedriver_win64\msedgedriver.exe"

    # Criando o objeto de opções do Edge
    options = EdgeOptions()

    # Habilitando o Chromium-based Edge
    options.use_chromium = True

    # Configurações de modo anônimo e desabilitação de recursos
    options.add_argument("--inprivate")  # Habilita o modo anônimo
    options.add_argument("--disable-features=Identity")  # Desabilita a autenticação implícita
    options.add_argument("--disable-identity-provider")  # Desabilita provedor de identidade
    options.add_argument("--disable-sync")  # Desabilita a sincronização do navegador
    options.add_argument("--disable-extensions")  # Desabilita extensões do navegador
    options.add_argument("--disable-logging")  # Desabilita logs internos do navegador
    options.add_argument("--no-first-run")  # Impede execução de inicialização do primeiro uso
    options.add_argument("--no-default-browser-check")  # Impede checagem de navegador padrão
    options.add_argument(f"--user-data-dir={diretorio_temp}")  # Usar o diretório temporário
    options.add_argument("--remote-debugging-port=9222")  # Ativa a porta de depuração

    # Capabilities com as opções
    capabilities = options.to_capabilities()

    # Inicializa o WebDriver com as capabilities
    try:
        driver = webdriver.Edge(executable_path=driver_path, capabilities=capabilities)

        # Configura o objeto wbot
        wbot.driver_path = driver_path
        wbot.browser = "EDGE"
        wbot.driver = driver

        print("Navegador iniciado com sucesso!")
        return driver

    except Exception as e:
        print(f"Erro ao iniciar o navegador: {e}")
        raise Exception("Falha ao iniciar o navegador com as configurações especificadas")
