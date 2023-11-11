import oracledb

def getConnection(user, password, host, port, service_name):
    try:
        connection = oracledb.connect(user=user, password=password, host=host, port=port, service_name=service_name)
        print(f'Conexão : {connection.version}')
    except Exception as e:
        print('Erro ao obter a conexão', e)
    return connection

def closeConnection(connection):
    try:
        connection.close()
        print(f'Conexao encerrada!')
    except Exception as e:
        print(f"Algo ocorreu errado: {e}")

def insert(table, rows, values):
    try:
        conexao = getConnection()
        cursor = conexao.cursor()
        query = f"INSERT INTO {table} ({rows}) VALUES ({values})"
        cursor.execute(query)
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        print(f"Algo ocorreu errado: {e}")
    finally:
        closeConnection(conexao)
        print("Inserido com Sucesso")

def select(table):
    try:
        conexao = getConnection()
        cursor = conexao.cursor()
        query = f"SELECT * FROM {table}"
        cursor.execute(query)
        conexao.commit()
    except Exception as e:
        print(f"Algo ocorreu errado: {e}")
    finally:
        closeConnection(conexao)
        print("Resgatado com Sucesso")

def update(table, camps, id_row, id_value):
    try:
        conexao = getConnection()
        cursor = conexao.cursor()
        query = f"UPDATE {table} SET {camps} WHERE {id_row} = {id_value}"
        cursor.execute(query)
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        print(f"Algo ocorreu errado: {e}")
    finally:
        closeConnection(conexao)
        print("Atualizado com Sucesso")

def delete(table, id_row, id_value):
    try:
        conexao = getConnection()
        cursor = conexao.cursor()
        query = f"DELETE FROM {table} WHERE {id_row} = {id_value}"
        cursor.execute(query)
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        print(f"Algo ocorreu errado: {e}")
    finally:
        closeConnection(conexao)
        print("Deletado com Sucesso")

