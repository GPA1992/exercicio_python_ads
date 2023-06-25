from gerenciar_json import carregar_arquivo, salvar_arquivo


def exibir_dado(nome_dado):
    dados_totais = carregar_arquivo()
    dados = dados_totais[nome_dado]
    for dado in dados:
        print(dado)


def adicionar_dado(nome_dado, novo_dado):
    dados_totais = carregar_arquivo()
    print(dados_totais)
    dados = dados_totais[nome_dado]
    dados.append(novo_dado)
    salvar_arquivo(dados_totais)


disc = {"codigo": 1, "nome": "Matemática"}


adicionar_dado("disciplinas", disc)
exibir_dado("disciplinas")
