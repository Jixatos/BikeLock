from Funcoes.functions import inputEmail, inputPassword, login, cadastroClient, inputTelefone, inputCep, inputCpf, \
    inputCnpj, GETViaCep, verCep, connectionJSON
from DataBase.crud import getConnection, closeConnection

#Variaveis de controle
test = True

while test:

    print("Olá, Bem-vindo a BikeLock")
    print("Para iniciar, insira os dados para conexão com banco de dados. Tenha em mente que você já deve ter "
          "aberto o SQL Developer e rodado o script para funcionar adequadamente.")

    connection_input = connectionJSON('connection.json')

    print("Faça seu login")
    status_login = ''
    while status_login != 'logado':
        email = inputEmail()
        senha = inputPassword()
        print(connection_input)
        status_login = login(connection_input, email, senha)
        if status_login == 'login':
            status_login = 'logado'
        else:
            print("Você já possui um cadastro? Caso não possua, digite 'Cadastrar'.\nCaso você já possua um cadastro "
                  "digite qualquer coisa para sair")
            cad = input("Digite: ").strip().upper()
            if cad == 'CADASTRAR':
                usuario = {'nome': input("Nome: "),
                           'email': inputEmail(),
                           'telefone': inputTelefone(),
                           'senha': inputPassword()}
                cont = False
                while not cont:
                    fis_jud = input(
                        "Pessoa fisíca ou jurídica? Responda com 'F' para física e 'J' para jurídica\nR: ").strip().upper()
                    match fis_jud:
                        case 'F':
                            usuario['cpf'] = inputCpf()
                            usuario['cnpj'] = None
                            cont = True
                        case 'J':
                            usuario['cpf'] = None
                            usuario['cnpj'] = inputCnpj()
                            cont = True
                        case _:
                            print("Por favor, insira uma opção válida.")
                cep_input = False
                while not cep_input:
                    cep = inputCep()
                    dic = GETViaCep(cep)
                    if verCep(dic):
                        endereco = {'cep': cep,
                                    'logradouro': dic['logradouro'],
                                    'numero': input('Numero: '),
                                    'complemento': dic['complemento'],
                                    'estado': input('Estado: '),
                                    'cidade': input('Cidade: ')}
                        while type(endereco['numero']) != int:
                            print("Digite um número válido")
                            endereco['numero'] = input("Número")
                        cep_input = True
                    else:
                        cep_manual = False
                        while not cep_manual:
                            repeat_cep = input("Quer inserir manualmente o CEP? Responda com Sim ou Não").strip().upper()
                            match repeat_cep:
                                case 'SIM' | 'S':
                                    endereco = {'cep': cep,
                                                'logradouro': input("Logradouro: "),
                                                'numero': input('Numero: '),
                                                'complemento': input("Complemento: "),
                                                'estado': input('Estado: '),
                                                'cidade': input('Cidade: ')}
                                    while type(endereco['numero']) != int:
                                        print("Digite um número válido")
                                        endereco['numero'] = input("Número")
                                    cep_input = True
                                case 'NÃO' | 'NAO' | 'N':
                                    print("Insira o CEP novamente: ")
                                case _:
                                    print("Responda apenas com Sim ou Não")
                usuario['endereco'] = endereco
                cadastroClient(connection_input, usuario)
