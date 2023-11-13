from DataBase.crud import insert, select, getConnection, closeConnection
import requests
import json
import os


def inputTelefone():
    try:
        ddd = int(input("DDD: "))
        numero = input("Telefone: ")

        # (Regex)

        numero = int(numero.strip())
        telefone = f'{ddd}{numero}'

        return telefone
    except ValueError as e:
        print("Erro de entrada no Telefone: ", e)
        return None


def inputCpf():
    try:
        while True:
            cpf = input("CPF: ")

            car = ".-/ "
            for i in range(0, len(car)):
                cpf = cpf.replace(car[i], "")
            if len(cpf) == 11:
                return cpf
    except Exception as e:
        print("Erro de entrada no CPF: ", e)
        return None


def inputCnpj():
    try:
        while True:
            cnpj = input("CPF: ")

            car = ".-/ "
            for i in range(0, len(car)):
                cnpj = cnpj.replace(car[i], "")
            if len(cnpj) == 11:
                return cnpj
    except Exception as e:
        print("Erro de entrada no CNPJ: ", e)
        return None


def inputEmail():
    try:
        email = input("Email: ")

        # (Regex)

        return email

    except Exception as e:
        print("Erro de entrada no Email: ", e)
        return None


def inputPassword():
    try:
        senha = input("Senha: ")
        # (Regex)

        return senha
    except Exception as e:
        print("Erro na entrada da Senha: ", e)
        return None


def inputCep():
    try:
        cep = input("CEP: ")

        # (REGEX)
        car = ".-/ "
        for i in range(0, len(car)):
            cep = cep.replace(car[i], "")

        return cep
    except Exception as e:
        print("Erro de entrada no CPF: ", e)
        inputCep()


def inputNumero():
    try:
        numero = int(input("Numero: "))
        return numero
    except ValueError as ve:
        print("Erro de entrada no numero: ", ve)
        inputNumero()
    except Exception as e:
        print("Erro de entrada do número: ", e)


def inputEstado():
    try:
        estado = input("Estado: ")
        if len(estado) == 2:
            return estado
        else:
            inputEstado()
    except Exception as e:
        print("Erro de entrada de Estado: ", e)


def inputValor():
    try:
        valor = input("Valor: ")
        valor = float(valor.replace(',', '.'))
        return valor
    except ValueError:
        print("Digite um valor válido.")
        inputValor()
    except Exception as e:
        print("Erro de entrada no valor: ", e)


def GETViaCep(cep):
    try:
        url = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(url)
        dic = requisicao.json()
        return dic
    except Exception as e:
        print("Erro no GETCep: ", e)


def verCep(dic):
    try:
        cep = dic['cep']
        if cep is not None:
            return True
    except KeyError:
        print("O CEP foi digitado errado ou é inexistente")
        return False
    except Exception as e:
        print("Erro com o Objeto JSON recuperado pelo ViaCEP: ", e)


def cadastroClient(connection_input, usuario):
    try:
        str_rows_user = 'email, nome, telefone, senha'

        email = usuario['email']
        nome = usuario['nome']
        telefone = usuario['telefone']
        senha = usuario['senha']
        values_user = f"'{email}','{nome}','{telefone}','{senha}'"

        cpf = usuario['cpf']
        rg = usuario['rg']
        values_fis = f"'{cpf}','{rg}','{email}'"

        cnpj = usuario['cnpj']
        values_jud = f"'{cnpj}','{email}'"

        endereco = usuario['endereco']
        rows_end = [rows for rows in endereco.keys()]
        str_rows_end = ",".join(rows_end)

        cep = endereco['cep']
        logradouro = endereco['logradouro']
        numero = endereco['numero']
        complemento = endereco['complemento']
        estado = endereco['estado']
        cidade = endereco['cidade']
        values_end = f"'{cep}','{logradouro}',{numero},'{complemento}','{estado}','{cidade}','{email}'"

        # Inserção na tabela de cliente
        insert(connection_input, 'cliente', str_rows_user, values_user)

        # Inserção na tabela de endereco
        insert(connection_input, 'endereco', str_rows_end, values_end)

        # Inserção na tabela Fisica/Jurídica
        if cpf is not None:
            insert(connection_input, 'fisica', 'cpf, rg, cliente_email', values_fis)
        else:
            insert(connection_input, 'judicial', 'cnpj, cliente_email', values_jud)

        print("Cadastrado com sucesso!")
        return 1
    except Exception as e:
        print("Erro no cadastro do usuário: ", e)


def login(connection_input, email, senha):
    try:
        rows = select(connection_input, 'cliente', 'email', email)
        if rows and len(rows) > 0:
            if email == rows[0][0] and senha == rows[0][3]:
                print("Login efetuado com Sucesso!")
                return 'logado'
            else:
                print("Email ou senha incorreto.")
                return 'deslogado'
        else:
            print("Nenhum resultado encontrado.")
            return 'deslogado'
    except Exception as e:
        print("Erro no login: ", e)


def writeJSON(dic, file):
    with open(file, "w") as file_json:
        json.dump(dic, file_json)


def createJSON(file):
    c = 0
    connection_input = {}
    while c != 1:
        connection_input = {"user": input("User: "),
                            "password": input("Password: "),
                            "host": input("Host: "),
                            "port": input("Port: "),
                            "service_name": input("Service_name: ")}
        writeJSON(connection_input, file)
        connect = getConnection(connection_input)
        if connect != 'Error':
            closeConnection(connect)
            writeJSON(connection_input, 'connection.json')
            print("Dados corretos para conexão, arquivo de conexão salvo.")
            c = 1
        else:
            print("Dados incorretos para conexão. Insira-os corretamente")
    return connection_input


def connectionJSON(file):
    if os.path.exists(file):
        with open(file, "r") as arq_json:
            connection_input = json.load(arq_json)
            return connection_input
    else:
        connection_input = createJSON(file)
        return connection_input


def segurosPrint():
    print("Os seguros disponibilizados pela PortoSeguros são:"
          "\nPedal Essencial - O plano gratuito* para você experimentar um dos serviços essenciais oferecidos, "
          "de acordo com as suas necessidades."
          "\nPedal Leve - Você gosta de pedalar e está buscando um plano de serviços intermediário? O Pedal leve da "
          "Porto é para você."
          "\nPedal Elite - Conte com diversos serviços capazes de elevar suas aventuras para o próximo nível.")
    seguros = ['Pedal Essencial', 'Pedal Leve', 'Pedal Elite']
    return seguros


def cadastroBike(connection_input, email, bike):
    try:
        marca = bike['marca']
        modelo = bike['modelo']
        valor = bike['valor']
        str_rows = "marca, modelo, valor, cliente_email"
        str_values = f"'{marca}', '{modelo}', {valor}, '{email}'"

        insert(connection_input, "bicicleta", str_rows, str_values)
        return 1
    except Exception as e:
        print("Erro no cadastro da Bike: ", e)


def logoff():
    conf = input("Você quer se desconectar? Responda com 'Sim' ou 'Não\nR:'").strip().upper()
    match conf:
        case 'SIM' | 'S':
            return 'deslogado'
        case 'NÃO' | 'NAO' | 'N':
            return 'logado'


def turnOFF():
    conf = input("Você quer SAIR? Caso queira sair digite 'SAIR'\nR: ")
    match conf:
        case 'SAIR':
            print("Tudo bem. Muito obrigado por usar nossos serviços.")
            return False
        case _:
            return True


def verificarBicicleta(connection_input, email):
    try:
        array = select(connection_input, "bicicleta", 'cliente_email', email)
        id = array[0][0]
        return id
    except IndexError as ie:
        print("Erro no select do id da bike,", ie)
    except Exception as e:
        print("Erro na verificação da bicicleta do cliente: ", e)


def insertSeguro(connection_input, email, seguro):
    try:
        id_bicicleta = verificarBicicleta(connection_input, email)

        str_rows = "seguro, id_bicicleta"
        str_values = f"'{seguro}', '{id_bicicleta}'"

        insert(connection_input, 'seguros', str_rows, str_values)

    except Exception as e:
        print("Erro na escolha de seguro: ", e)


def perfil(connection_input, email):
    try:
        user = select(connection_input, 'cliente', 'email', email)
        print(f"Nome: {user[0][1]}"
              f"\nEmail: {email}"
              f"\nTelefone: {user[0][2]}")
        cpf = select(connection_input, 'fisica', 'cliente_email', email)
        cnpj = select(connection_input, 'judicial', 'cliente_email', email)
        if len(cnpj) == 0:
            print(f"CPF: {cpf[0][0]}"
                  f"\nRG: {cpf[0][1]}")
        else:
            print(f"CNPJ: {cnpj[0][0]}")

        endereco = select(connection_input, 'endereco', 'cliente_email', email)
        print(f"CEP: {endereco[0][1]}"
              f"\nEndereco: {endereco[0][2]} - {endereco[0][3]}"
              f"\nComplemento: {endereco[0][4]}"
              f"\nLocalidade: {endereco[0][6]} - {endereco[0][5]}")

        bike = select(connection_input, 'bicicleta', 'cliente_email', email)
        print(f"Bike"
              f"\nMarca: {bike[0][1]}"
              f"\nModelo: {bike[0][2]}"
              f"\nValor: {bike[0][3]}")
    except Exception as e:
        print("Erro no retorno dos dados do usuário: ", e)
