from DataBase.crud import select
from Funcoes.functions import (inputEmail, inputPassword, login, cadastroClient, inputTelefone, inputCep, inputCpf,
                               inputCnpj, GETViaCep, verCep, connectionJSON, inputNumero, inputEstado, segurosPrint,
                               cadastroBike, inputValor, logoff, turnOFF, insertSeguro, perfil)

#Arquivo de demonstração da página do FrontEnd com o BackEnd feito em python, funções principais e demais: "Funcoes/funtions.py"

# Variaveis de controle para simulação
test = True  # apenas para o while e simular uma aplicação
status_login = 'deslogado'
print("Olá, Bem-vindo a BikeLock")
print("Para iniciar, insira os dados para conexão com banco de dados. Tenha em mente que você já deve ter "
      "aberto o SQL Developer e rodado o script para funcionar adequadamente.")
while test:

    connection_input = connectionJSON('connection.json')
    while status_login != 'logado':

        # Página de Login
        print("Faça seu login")

        # Simulação do formulário de entrada de dados do usuário para o Login
        email = inputEmail()
        senha = inputPassword()
        status_login = login(connection_input, email, senha)
        if status_login != 'logado':
            print("Você já possui um cadastro? Caso não possua, digite 'Cadastrar'.\nCaso você já possua um cadastro "
                  "digite qualquer coisa para sair")
            cad = input("Digite: ").strip().upper()
            if cad == 'CADASTRAR':

                # Página de Cadastro
                cond_cad = 0
                while cond_cad != 1:
                    print("Cadastro")
                    # Simulação do formulário de entrada de dados do usuário para o cadastro
                    cliente = {'nome': input("Nome: "),
                               'email': inputEmail(),
                               'telefone': inputTelefone(),
                               'senha': inputPassword()}
                    cont = False
                    while not cont:

                        # Confirmação de pessoa física ou pessoa jurídica
                        pessoa_doc = input(
                            "Pessoa fisíca ou jurídica? Responda com 'F' para física e 'J' para jurídica\nR: ").strip().upper()

                        # Fomulário de entrada do CPF ou CNPJ
                        match pessoa_doc:
                            case 'F':
                                # Formulário CPF

                                cliente['cpf'] = inputCpf()
                                cliente['rg'] = input("RG: ")
                                cliente['cnpj'] = None
                                cont = True
                            case 'J':
                                # Formulário CNPJ

                                cliente['cpf'] = None
                                cliente['cnpj'] = inputCnpj()
                                cont = True
                            case _:
                                print("Por favor, insira uma opção válida.")

                    # Após informar o dados do usuário agora o endereço
                    cep_input = False
                    while not cep_input:
                        # Formulário de entrada para o CEP
                        cep = inputCep()
                        dic = GETViaCep(cep)  # Recuperando dados pelo ViaCEP
                        if verCep(dic):
                            # Formulário de entrada do endereço preenchido quase completo pelo CEP (GETViaCep)
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

                                        # Formulário de entrada para o endereço para casos manuais
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
            # Página Principal, na qual seria a visualização com seu login efetuado (nome e dados)
            user = select(connection_input, 'cliente', 'email', email)
            print(f"Parabéns, {user[0][1]} você está logado.")

    # Um cabeçalho com as opções de Entrada para o usuário
    print("Para prosseguir com as escolhas abaixo escolha o número referente a opção desejada.")
    escolha = input("Página principal - 'HOME'"
                    "\n1 > Seguros de Bikes "
                    "\n2 > Bike cadastro"
                    "\n3 > Selecionar Seguro"
                    "\n4 > Perfil"
                    "\n5 > LogOFF"
                    "\n6 > Sair"
                    "\nR: ")
    # Encaminhamento para a página desejada
    match escolha:
        case '1':
            segurosPrint()  # Página dos seguros, apenas vizualização
        case '2':
            cad_bike = 0
            while cad_bike != 1:
                # Página de cadastro da Bike
                #Formulário de entrada da bike
                bike = {'marca': input("Marca: "),
                        'modelo': input("Modelo: "),
                        'valor': inputValor(),
                        'email': email}

                cad_bike = cadastroBike(connection_input, email, bike)
        case '3':
            esc_sec = False
            while not esc_sec:
                # Página de Escolha de seguro para a bicicleta
                seguros = segurosPrint()
                seguro = input("Para escolher entre um deles basta escrever o nome da mesma forma que está abaixo\n"
                               "Exemplo: Pedal Essencial\nR: ")
                if seguro in seguros:
                    insertSeguro(connection_input, email, seguro)
                    esc_sec = True
                else:
                    print("Escolha um entre os seguros mostrados")
        case '4':
            perfil(connection_input, email) # Página de perfil do usuário e demais informações
        case '5':
            status_login = logoff() # Página de logoff
        case '6':
            test = turnOFF() # Fechar a página, fechar a aplicação
        case _:
            print('Insira um número entre o menu mostrado acima:')
