import getpass

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
        return email
        # (Regex)

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

