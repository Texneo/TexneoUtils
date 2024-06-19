from botcity.web.browsers.edge import default_options
import os

def configurar_EDGE(wbot):

    """
    
    Prepara EDGE para aexecução padrão.

    ->
    wbot: Instância do web bot ativa.
    
    """

    def_options = default_options()
    def_options.add_argument("--remote-debugging-port=9999")
    def_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    def_options.add_experimental_option('prefs', {'browser':{'show_hub_popup_on_download_start': False}})
    wbot.options = def_options

def mover_arquivo(origem, destino, nome_origem, nome_destino):

    """
    
    Move arquivos entre diretórios.

    ->
    origem: Diretório de origem do arquivo.
    destino: Diretório destivo do arquivo.
    nome_origem: Nome do arquivo na pasta origem.
    nome_destino: Nome do arquivo na pasta destino.

    """

    os.rename(f"{origem}\{nome_origem}", f"{destino}\{nome_destino}")

def valida_diretorios(lista_diretorios):

    """
    
    Valida disponibilidade de uma lista de diretórios. (Estoura exception em caso de erro de acesso.)

    ->
    lista_diretorios: Lista de diretórios a validar.

    """

    for diretorio in lista_diretorios:

        os.listdir(diretorio)