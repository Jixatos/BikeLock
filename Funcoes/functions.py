from DataBase.crud import insert, select, update, delete
import getpass
import requests

def inputTelefone():
    try:
        ddd = int(input("DDD: "))
        numero = input("Telefone: ")
        ddd = ddd.strip()

        # (Regex)

        numero = int(numero.strip())
        telefone = (ddd, numero)

        return telefone
    except ValueError as e:
        print("Erro de entrada no Telefone: ", e)
        return None

def inputCpf():
    try:
        cpf = input("CPF: ")

        # Remoção de caracteres padrões no CPF (Regex)
        car = ".-/ "
        for i in range(0, len(car)):
            cpf = cpf.replace(car[i], "")
        cpf = int(cpf)

        return cpf
    except Exception as e:
        print("Erro de entrada no CPF: ", e)
        return None

def inputCnpj():
    try:
        cnpj = input("CNPJ: ")

        # Remoção de caracteres padrões no CNPJ (Regex)
        car = ".-/ "
        for i in range(0, len(car)):
            cnpj = cnpj.replace(car[i], "")
        cnpj = int(cnpj)

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
        senha = getpass.getpass("Senha: ")
        # (Regex)

        return senha
    except Exception as e:
        print("Erro na entrada na Senha: ", e)
        return None

def inputCep():
    try:
        cep = input("CEP: ")

        # (REGEX)
        car = ".-/ "
        for i in range(0, len(car)):
            cep = cep.replace(car[i], "")
        cep = int(cep)

        return cep
    except Exception as e:
        print("Erro de entrada no CPF: ",e)

def GETViaCep(cep):
    try:
        url = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(url)
        dic = requisicao.json()
        return dic
    except Exception as e:
        print("Erro no GETCep: ",e)

def verCep(dic):
    try:
        cep = dic['cep']
        if cep is not None:
            return True
    except KeyError:
        print("O CEP foi digitado errado ou é inexistente")
        return False
    except Exception as e:
        print("Erro com o Objeto JSON recuperado pelo ViaCEP: ",e)

def cadastroClient(usuario):
    try:
        rows_user = [row for row in usuario.keys()]
        str_rows_user = ",".join(rows_user)

        email = usuario['email']
        nome = usuario['nome']
        telefone = usuario['telefone']
        senha = usuario['senha']
        values_user = f'{email},{nome},{telefone},{senha}'

        cpf = usuario['cpf']
        rg = usuario['rg']
        values_fis = f'{cpf},{rg}'

        cnpj = usuario['cnpj']
        values_jud = f'{cnpj}'

        endereco = usuario['endereco']
        rows_end = [rows for rows in endereco.keys()]
        str_rows_end = ",".join(rows_end)

        cep = endereco['cep']
        rua = endereco['rua']
        numero = endereco['numero']
        complemento = endereco['complemento']
        estado = endereco['estado']
        cidade = endereco['cidade']
        values_end = f'{cep},{rua},{numero},{complemento},{estado},{cidade}'

        #Inserção na tabela de endereco
        insert('endereco',str_rows_end,values_end)

        #Inserção na tabela de cliente
        insert('cliente',str_rows_user,values_user)

        #Inserção na tabela Fisica/Jurídica
        if cpf is not None:
            insert('fisica','cpf, rg', values_fis)
        else:
            insert('judicial', 'cnpj', values_jud)

        print("Cadastrado com sucesso!")
    except Exception as e:
        print("Erro no cadastro do usuário: ",e)

def login(email, senha):
    try:
        tuple = select('cliente', 'email', email)
        if email == tuple[0] and senha == tuple[3]:
            return True
        else:
            return False
    except Exception as e:
        print("Erro no login: ", e)