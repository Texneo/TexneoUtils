from botcity.web import Browser
from botcity.web.browsers.edge import default_options
from tqdm import tqdm
from packaging.version import Version

import requests, os, zipfile



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

    baixar_ultima_versao_edge_driver()

    def_options = default_options(
        headless=wbot.headless,
        download_folder_path="C:\\Users\\bot-python-01\\Downloads",
        user_data_dir=None,  # Informing None here will generate a temporary directory
    )
    def_options.add_argument("--inprivate")
    def_options.add_argument("--log-level=3")

    # Evita popups e prompts de download
    def_options.add_experimental_option('prefs', {'browser':{'show_hub_popup_on_download_start': False}})

    wbot.options = def_options

    # Definindo navegador como EDGE
    wbot.browser = Browser.EDGE

    wbot.driver_path = "C:\\Driver Edge\\edgedriver_win64\\msedgedriver.exe"

    wbot.headless = False

def obter_versao_mais_recente():
    url = "https://edgeupdates.microsoft.com/api/products?view=enterprise"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    latest = None

    for product in data:
        if product["Product"] == "Stable":
            for release in product.get("Releases", []):
                if release["Platform"] == "Windows" and release["Architecture"] == "x64":
                    version = Version(release["ProductVersion"])
                    if not latest or version > latest:
                        latest = version
    return latest
    
def baixar_driver(url, dest_path):

    response = requests.get(url, stream=True)
    total = int(response.headers.get('content-length', 0))
    with open(dest_path, 'wb') as file, tqdm(
        desc="Baixando WebDriver",
        total=total,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            file.write(data)
            bar.update(len(data))

def extrair_zip(zip_path, extract_to):

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def baixar_ultima_versao_edge_driver(dest_dir="C:\\Driver Edge\\edgedriver_win64"):
    version = obter_versao_mais_recente()
    print(f"Última versão estável do WebDriver: {version}")

    url = f"https://msedgedriver.microsoft.com/{version}/edgedriver_win64.zip"
    zip_path = os.path.join(dest_dir, "edgedriver.zip")

    os.makedirs(dest_dir, exist_ok=True)
    baixar_driver(url, zip_path)
    extrair_zip(zip_path, dest_dir)
    os.remove(zip_path)
    print(f"Driver baixado e extraído em: {dest_dir}")
