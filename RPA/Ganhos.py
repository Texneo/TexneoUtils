from sqlalchemy import create_engine, Table, MetaData, insert
from urllib.parse import quote_plus
from datetime import datetime

def registrar_ganho(db_username, db_password, db_server, db_database, task, codigo_robo, segundos_economizados):

    """
    Registra ganhos de execução do RPA. 

    (Método Temporário)

    ->
    wbot: Instância do web bot ativa.
    """

    # Cria a engine de conexão
    engine = create_engine(f"mssql+pymssql://{db_username}:%s@{db_server}/{db_database}" % quote_plus(db_password))
    
    # Conecta ao banco de dados
    connection = engine.connect()
    
    # Defina a tabela onde o insert será realizado
    metadata = MetaData()
    tabela_ganhos = Table('GanhosEstimados', metadata, autoload_with=engine)
    
    # Dados a serem inseridos
    dados = {
        'task': task,
        'codigo_robo': codigo_robo,
        'segundos_economizados': segundos_economizados,
        'data': datetime.now()
    }
    
    # Realiza o insert
    inserir = insert(tabela_ganhos).values(dados)
    connection.execute(inserir)

    # Persiste os dados
    connection.commit()
    
    # Fecha a conexão
    connection.close()