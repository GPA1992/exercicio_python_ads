from gerenciar_json import carregar_arquivo, salvar_arquivo


def listar_todos(nome_dado):
    dados_totais = carregar_arquivo()
    dados = dados_totais[nome_dado]
    if dados_totais["alunos"] is not None:
        for dado in dados:
            nome = dado["nome"]
            print(f"Nome: {nome}")


def incluir(nome_dado, novo_dado):
    dados_totais = carregar_arquivo()
    dados = dados_totais[nome_dado]
    ultimo_dado = dados[-1]
    codigo = ultimo_dado["codigo"]
    novo_dado["codigo"] = codigo + 1
    dados.append(novo_dado)
    salvar_arquivo(dados_totais)
