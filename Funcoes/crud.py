import oracledb

def getConnection():
    try:
        connection = oracledb.connect(user="RM551408", password="110804", host="oracle.fiap.com.br", port=1521, service_name="orcl")
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

def insert(tabela, ident, campo, valor):
    try:
        conexao = getConnection()
        cursor = conexao.cursor()
        query = f"INSERT INTO {tabela} SET {ident} WHERE {campo} = {valor}"
        cursor.execute(query)
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        print(f"Algo ocorreu errado: {e}")
    finally:
        closeConnection(conexao)
        print("Inserido com Sucesso")

def select(tabela):
    try:
        conexao = getConnection()
        cursor = conexao.cursor()
        query = f"SELECT * FROM {tabela}"
        cursor.execute(query)
        conexao.commit()
    except Exception as e:
        print(f"Algo ocorreu errado: {e}")
    finally:
        closeConnection(conexao)
        print("Resgatado com Sucesso")

def update(tabela, campo, valor, ident, id_valor):
    try:
        conexao = getConnection()
        cursor = conexao.cursor()
        query = f"UPDATE {tabela} SET {campo} = {valor} WHERE {ident} = {id_valor}"
        cursor.execute(query)
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        print(f"Algo ocorreu errado: {e}")
    finally:
        closeConnection(conexao)
        print("Atualizado com Sucesso")

def delete(tabela, ident, valor):
    try:
        conexao = getConnection()
        cursor = conexao.cursor()
        query = f"DELETE FROM {tabela} WHERE {ident} = {valor}"
        cursor.execute(query)
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        print(f"Algo ocorreu errado: {e}")
    finally:
        closeConnection(conexao)
        print("Deletado com Sucesso")

