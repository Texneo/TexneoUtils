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
    import os, time, traceback

    diretorio_temp = os.path.join(os.getcwd(), "temp")
    os.makedirs(diretorio_temp, exist_ok=True)

    driver_path = r"C:\Users\bot-python-01\Desktop\edgedriver_win64\msedgedriver.exe"

    options = EdgeOptions()
    options.use_chromium = True  # Apenas se for Chromium-based Edge

    # Como não há .add_argument(), usamos desired_capabilities
    # Criação dos capabilities de forma direta
    capabilities = options.to_capabilities()
    capabilities = {
        "browserName": "MicrosoftEdge",
        "platform": "WINDOWS",
        "ms:edgeOptions": {
            "args": [
                "--inprivate",  # Habilita o modo anônimo
                "--disable-features=Identity",  # Desabilita a autenticação implícita
                "--disable-identity-provider",  # Desabilita provedor de identidade
                "--disable-sync",  # Desabilita a sincronização do navegador
                "--disable-extensions",  # Desabilita extensões do navegador
                "--disable-logging",  # Desabilita logs internos do navegador
                "--no-first-run",  # Impede execução de inicialização do primeiro uso
                "--no-default-browser-check",  # Impede checagem de navegador padrão
                f"--user-data-dir={diretorio_temp}",  # Usar o diretório temporário
                "--remote-debugging-port=9222"  # Ativa a porta de depuração
            ]
        }
    }

    for tentativa in range(1, max_tentativas + 1):
        try:
            print(f"Tentativa {tentativa}/{max_tentativas} de iniciar EdgeDriver...")

            # Sem options, usamos apenas capabilities
            driver = webdriver.Edge(executable_path=driver_path, capabilities=capabilities)

            wbot.driver_path = driver_path
            wbot.browser = "EDGE"
            wbot.driver = driver

            print("Navegador iniciado com sucesso!")
            return

        except Exception:
            print(f"Erro ao iniciar o EdgeDriver na tentativa {tentativa}:")
            traceback.print_exc()
            #try:
            #   driver.quit()
            #except:
            #    pass
            time.sleep(espera)

    raise RuntimeError(f"Não foi possível iniciar o navegador após {max_tentativas} tentativas.")
