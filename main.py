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
