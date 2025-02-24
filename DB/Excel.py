from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from openpyxl import Workbook
import pandas

def exportar_SQL_para_TXT(caminho_arquivo, db_server, db_database, db_username, db_password, db_tabela, db_schema, delimitador):

    """
    
    Exporta uma tabela do banco SQL Server para um arquivo TXT. 
    Este método espera que o nome das colunas no arquivo Excel seja o mesmo nome na coluna dentro da tabela no banco de dados.

    ->
    caminho_arquivo: Caminho do arquivo TXT que se deseja gerar.
    db_server: Servidor do banco de dados.
    db_database = Nome da database.
    db_username = Username.
    db_password = Password.
    db_tabela = Tabela para exportar os dados.
    db_schema = Schema da tabela.
    delimitador = separador das colunas dento do TXT.
    
    """
    
    # Configuração do banco de dados
    engine = create_engine(f"mssql+pymssql://{db_username}:{quote_plus(db_password)}@{db_server}/{db_database}")

    # Query para buscar os dados do banco
    query = f"SELECT * FROM {db_schema}.{db_tabela}"

    chunk_size = 10000 

    # Definir o encoding para garantir que a acentuação seja preservada
    encoding = "utf-8-sig"

    # Inicializar a variável para controlar se o cabeçalho já foi escrito
    header_written = False

    # Lendo os dados em chunks e escrevendo no arquivo CSV
    for chunk in pandas.read_sql_query(query, engine, chunksize=chunk_size):
        chunk.to_csv(caminho_arquivo, mode='a', index=False, header=not header_written, sep=delimitador, encoding=encoding)

        header_written = True

def exportar_SQL_para_XLSX(caminho_arquivo, db_server, db_database, db_username, db_password, db_tabela, db_schema):

    """
    
    Exporta uma tabela do banco SQL Server para um arquivo XLSX. 
    Este método espera que o nome das colunas no arquivo Excel seja o mesmo nome na coluna dentro da tabela no banco de dados.

    ->
    caminho_xlsx: Caminho do arquivo XLSX que se deseja gerar.
    db_server: Servidor do banco de dados.
    db_database = Nome da database.
    db_username = Username.
    db_password = Password.
    db_tabela = Tabela para exportar os dados.
    db_schema = Schema da tabela.
    
    """
    # Configuração do banco de dados
    engine = create_engine(f"mssql+pymssql://{db_username}:{quote_plus(db_password)}@{db_server}/{db_database}")

    # Query para buscar os dados do banco
    query = f"SELECT * FROM {db_schema}.{db_tabela}"

    # Criar um workbook novo e uma planilha de trabalho
    wb = Workbook()
    ws = wb.active
    ws.title = "Export"

    # Definir o tamanho do bloco de dados
    chunk_size = 10000  # Ajuste o tamanho conforme necessário

    # Inicializar a variável para controlar se o cabeçalho já foi escrito
    header_written = False

    # Lendo os dados em chunks e escrevendo no arquivo Excel
    for chunk in pandas.read_sql_query(query, engine, chunksize=chunk_size):
        for index, row in chunk.iterrows():
            if not header_written:
                # Escrever cabeçalho (apenas na primeira iteração)
                ws.append(chunk.columns.tolist())  # Usar as colunas como cabeçalho
                header_written = True
            
            # Escrever a linha de dados no arquivo Excel
            ws.append(row.tolist())
        
        # Salvar o arquivo após cada chunk (garantir que o arquivo parcial seja gravado)
        wb.save(caminho_arquivo)

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

    Session = sessionmaker(bind=engine)
    session = Session()

    engine = create_engine(f"mssql+pymssql://{db_username}:%s@{db_server}/{db_database}" % quote_plus(db_password))
    
    with session.begin():
        excel = pandas.read_excel(caminho_arquivo)
        excel.to_sql(db_tabela, con=engine, schema=db_schema, if_exists=if_exists)

    session.commit()

def importar_XLSX_para_SQL(caminho_arquivo, db_server, db_database, db_username, db_password, db_tabela, db_schema, db_sheet, db_columns, if_exists):

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
    db_sheet = Aba do Excel que deseja importar.
    db_columns = Colunas que deseja importar.
    if_exists = O que fazer em caso de a tabela já existir. ["append", "fail", "replace"]
    
    """

    # Dados de conexão
    engine = create_engine(f"mssql+pymssql://{db_username}:%s@{db_server}/{db_database}" % quote_plus(db_password))
    Session = sessionmaker(bind=engine)
    session = Session()

    with session.begin():
        # Leitura do Excel com a aba e as colunas específicas
        excel = pandas.read_excel(caminho_arquivo, sheet_name=db_sheet, usecols=db_columns)
        
        # Importando para o banco de dados
        excel.to_sql(db_tabela, con=engine, schema=db_schema, if_exists=if_exists, index=False)

    session.commit()
