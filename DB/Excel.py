from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas

def importar_XLSX_para_SQL(caminho_arquivo, db_server, db_database, db_username, db_password, db_tabela, db_schema, if_exists):

    """
    
    Faz o upload de dados de tabela Excel para dentro do banco SQL Server. 
    Este método espera que o nome das colunas no arquivo Excel seja o mesmo nome na coluna dentro da tabela no banco de dados.

    Necessário instalar Driver para realizar a conexão.

    ->
    caminho_xlsx: Caminho do arquivo XLSX que se deseja importar.
    db_server: Servidor do banco de dados.
    db_database = Nome da database.
    db_username = Username.
    db_password = Password.
    db_tabela = Tabela para inserir os dados.
    db_schema = Schema da tabela.
    if_exists = O que fazer em caso de a tabela já existir. ["append", "fail", "replace"]
    
    """

    engine = create_engine(f"mssql+pymssql://{db_username}:%s@{db_server}/{db_database}" % quote_plus(db_password))
    excel = pandas.read_excel(caminho_arquivo)
    excel.to_sql(db_tabela, con=engine, schema=db_schema, if_exists=if_exists)