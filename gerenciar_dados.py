from gerenciar_json import carregar_arquivo, salvar_arquivo


def listar_todos(nome_dado):
    try:
        if not isinstance(nome_dado, str):
            raise ValueError("O nome_dado deve ser uma string.")

        dados_totais = carregar_arquivo()
        dados = dados_totais[nome_dado]

        if dados_totais["alunos"] is not None:
            for dado in dados:
                nome = dado["nome"]
                cpf = dado["cpf"]
                codigo = dado["codigo"]
                print("-------------------------")
                print(f"Nome: {nome}")
                print(f"CPF: {cpf}")
                print(f"Código: {codigo}")
    except ValueError as error:
        print(f"Erro: {error}")


def incluir(nome_dado, novo_dado):
    try:
        if not isinstance(nome_dado, str):
            raise ValueError("O nome_dado deve ser uma string.")

        dados_totais = carregar_arquivo()
        dados = dados_totais[nome_dado]
        ultimo_dado = dados[-1]
        codigo = ultimo_dado["codigo"]
        novo_dado["codigo"] = codigo + 1
        dados.append(novo_dado)
        salvar_arquivo(dados_totais)
    except ValueError as error:
        print(f"Erro: {error}")
