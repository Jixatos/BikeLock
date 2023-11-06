import crud

def inputTelefone():
    try:
        ddd = int(input("DDD: "))
        numero = input("Telefone: ")

        numero = int(numero.strip())
        ddd = ddd.strip()
        telefone = (ddd, numero)

        return telefone
    except ValueError:
        print("Insira um valor válido")
        return 'ValueError'
    except Exception as e:
        print("Algo ocorreu errado", e)
        return None

def inputCpf():
    try:
        cpf = input("CPF: ")
        car = ".-/ "

        for i in range (0, len(car)):
            cpf = cpf.replace(car[i], "")
        cpf = int(cpf)

        return cpf
    except ValueError as e:
        print("Insira um valort válido", e)
        return "ValueError"
    except Exception as e:
        print("Algo ocorreu errado", e)
        return None
