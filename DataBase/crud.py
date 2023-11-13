import oracledb


def getConnection(connection_input):
    try:
        user = connection_input["user"]
        password = connection_input["password"]
        host = connection_input['host']
        port = connection_input['port']
        service_name = connection_input['service_name']
        connection = oracledb.connect(user=user, password=password, host=host, port=port, service_name=service_name)
        return connection
    except Exception as e:
        print('Erro na conexão com o BD: ', e)
        return 'Error'


def closeConnection(connection):
    try:
        connection.close()
    except Exception as e:
        print(f"Erro no fechamento da conexão com o BD: {e}")


def insert(connection_input, tabela, rows, values):
    try:
        conexao = getConnection(connection_input)
        cursor = conexao.cursor()
        query = f"INSERT INTO {tabela} ( {rows} ) VALUES ( {values} )"
        cursor.execute(query)
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        print("Erro no insert: ", e)
    finally:
        closeConnection(conexao)
        cursor.close()


def select(connection_input, tabela, id_row, value):
    try:
        conexao = getConnection(connection_input)
        cursor = conexao.cursor()
        query = f"SELECT * FROM {tabela} WHERE {id_row} = '{value}'"
        cursor.execute(query)
        array = [result for result in cursor]
    except Exception as e:
        print(f"Erro no select: {e}")
    finally:
        return array
        closeConnection(conexao)
        cursor.close()
