from Funcoes.functions import inputEmail, inputPassword, login, cadastroClient, inputTelefone, inputCep, inputCpf, \
    inputCnpj, GETViaCep, verCep

test = True
while test:
    print("Olá, Bem-vindo a BikeLock")
    print("Faça seu login")
    email = input("Email: ")
    senha = inputPassword()
    login = login(email, senha)
    if login:
        print("Login efetuado com Sucesso!")
    else:
        print("Erro no Login. Você já possui um cadastro? Caso não possua, digite 'Cadastrar'.\nCaso você já possua "
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

            cadastroClient(usuario)
