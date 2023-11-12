from Funcoes.functions import inputEmail, inputPassword, login, cadastroClient, inputTelefone, inputCep, inputCpf, inputCnpj, GETViaCep, verCep

test = True
while test:
    print("Olá, Bem-vindo a BikeLock")
    print("Faça seu login")
    email = inputEmail
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
            cont = 0
            while cont != 1:
                fis_jud = input(
                    "Pessoa fisíca ou jurídica? Responda com 'F' para física e 'J' para jurídica\nR: ").strip().upper()
                match fis_jud:
                    case 'F':
                        usuario['cpf'] = inputCpf()
                        usuario['cnpj'] = None
                        cont += 1
                    case 'J':
                        usuario['cpf'] = None
                        usuario['cnpj'] = inputCnpj()
                        cont += 1
                    case _:
                        print("Por favor, insira uma opção válida.")

            cep = inputCep()
            dic = GETViaCep(cep)
            if verCep(dic):
                endereco{'cep': cep,
                         'logradouro'}

            usuario['endereco'] = endereco

            cadastroClient(usuario)
