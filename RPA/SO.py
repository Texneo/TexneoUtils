import os

def valida_diretorios(lista_diretorios):

    """
    
    Valida disponibilidade de uma lista de diretórios. (Estoura exception em caso de erro de acesso.)

    ->
    lista_diretorios: Lista de diretórios a validar.

    """

    for diretorio in lista_diretorios:

        os.listdir(diretorio)