import os

def limpar_diretorios(lista_diretorios):

    """
    
    Remove todos os arquivos de uma lista de diretórios.

    ->
    lista_diretorios: Lista de string contendo os diretórios a serem esvaziados.

    """

    for diretorio in lista_diretorios:

        lista_arquivos = os.listdir(diretorio)

        for arquivo in lista_arquivos:

            os.remove(diretorio + "\\" + arquivo)


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