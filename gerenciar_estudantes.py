from gerenciar_json import carregar_arquivo, salvar_arquivo


def atualizar(codigo_aluno, aluno_atualizado):
    try:
        dados_totais = carregar_arquivo()
        alunos = dados_totais["alunos"]
        for aluno in alunos:
            if aluno["codigo"] == int(codigo_aluno):
                aluno["nome"] = aluno_atualizado["nome"]
                aluno["cpf"] = aluno_atualizado["cpf"]
                aluno["codigo"] = aluno_atualizado["codigo"]

        salvar_arquivo(dados_totais)
    except ValueError:
        print("O código do aluno deve ser um número.")


def excluir(codigo_aluno):
    try:
        dados_totais = carregar_arquivo()
        alunos = dados_totais["alunos"]

        for aluno in alunos:
            if aluno["codigo"] == int(codigo_aluno):
                alunos.remove(aluno)

        salvar_arquivo(dados_totais)
    except ValueError as error:
        print(error)
        return error
