from gerenciar_json import carregar_arquivo, salvar_arquivo


def atualizar(codigo_aluno, aluno_atualizado):
    dados_totais = carregar_arquivo()
    alunos = dados_totais["alunos"]
    for aluno in alunos:
        if aluno["codigo"] == int(codigo_aluno):
            aluno["nome"] = aluno_atualizado["nome"]
            aluno["cpf"] = aluno_atualizado["cpf"]
            aluno["codigo"] = aluno_atualizado["codigo"]
    salvar_arquivo(dados_totais)


def excluir(codigo_aluno):
    dados_totais = carregar_arquivo()
    alunos = dados_totais["alunos"]
    for aluno in alunos:
        if aluno["codigo"] == codigo_aluno:
            alunos.remove(aluno)
    salvar_arquivo(dados_totais)
