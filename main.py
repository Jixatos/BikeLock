from Funcoes.functions import inputEmail, inputPassword, login, cadastroClient, inputTelefone, inputCep, inputCpf, \
    inputCnpj, GETViaCep, verCep, connectionJSON, inputNumero, inputEstado
from DataBase.crud import select

# Variaveis de controle que seriam necessárias no front end
test = True #apenas para o while e simular uma aplicação
status_login = ''
print("Olá, Bem-vindo a BikeLock")
print("Para iniciar, insira os dados para conexão com banco de dados. Tenha em mente que você já deve ter "
      "aberto o SQL Developer e rodado o script para funcionar adequadamente.")
while test:

    connection_input = connectionJSON('connection.json')
    print("Faça seu login")
    while status_login != 'logado':
        email = inputEmail()
        senha = inputPassword()
        status_login = login(connection_input, email, senha)
        if status_login != 'logado':
            print("Você já possui um cadastro? Caso não possua, digite 'Cadastrar'.\nCaso você já possua um cadastro "
                  "digite qualquer coisa para sair")
            cad = input("Digite: ").strip().upper()
            if cad == 'CADASTRAR':
                cond_cad = 0
                while cond_cad != 1:
                    print("Cadastro")
                    cliente = {'nome': input("Nome: "),
                               'email': inputEmail(),
                               'telefone': inputTelefone(),
                               'senha': inputPassword()}
                    cont = False
                    while not cont:
                        pessoa_doc = input(
                            "Pessoa fisíca ou jurídica? Responda com 'F' para física e 'J' para jurídica\nR: ").strip().upper()
                        match pessoa_doc:
                            case 'F':
                                cliente['cpf'] = inputCpf()
                                cliente['rg'] = input("RG: ")
                                cliente['cnpj'] = None
                                cont = True
                            case 'J':
                                cliente['cpf'] = None
                                cliente['cnpj'] = inputCnpj()
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
                                        'numero': inputNumero(),
                                        'complemento': dic['complemento'],
                                        'estado': dic['uf'],
                                        'cidade': dic['localidade'],
                                        'cliente_email': cliente['email']}
                            cep_input = True
                        else:
                            cep_manual = False
                            while not cep_manual:
                                repeat_cep = input(
                                    "Quer inserir manualmente o endereço? Responda com Sim ou Não\nR:").strip().upper()
                                match repeat_cep:
                                    case 'SIM' | 'S':
                                        endereco = {'cep': inputCep(),
                                                    'logradouro': input("Logradouro: "),
                                                    'numero': inputNumero(),
                                                    'complemento': input("Complemento: "),
                                                    'estado': inputEstado(),
                                                    'cidade': input('Cidade: '),
                                                    'cliente_email': cliente['email']}
                                        cep_input = True
                                    case 'NÃO' | 'NAO' | 'N':
                                        cep_manual = True
                                    case _:
                                        print("Responda apenas com Sim ou Não")
                    cliente['endereco'] = endereco
                    cond_cad = cadastroClient(connection_input, cliente)
        else:
            user = select(connection_input, 'cliente', 'email', email)
            print(f"Parabéns, {user[0][1]} você está logado")




