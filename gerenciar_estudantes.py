from gerenciar_json import carregar_arquivo, salvar_arquivo
import acoes
import geral
from gerenciar_dados import listar_todos, incluir


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


def executar_acao_estudante(acao):
    geral.menu_acoes()
    if acao == "1":
        print(acoes.act1)
        estudante_nome = input("Digite o nome do novo estudante: ")
        estudante_cpf = input("Digite o CPF do novo estudante: ")
        incluir("alunos", {"nome": estudante_nome, "cpf": estudante_cpf})
        geral.mensagem_sucesso(estudante_nome)

    elif acao == "2":
        print(acoes.act2)
        print("Lista de Estudantes")
        listar_todos("alunos")
        print(geral.fim)

    elif acao == "3":
        print(acoes.act3)
        aluno_atualizar = input("Digite o código do estudante: ")
        try:
            aluno_atualizar = int(aluno_atualizar)
            if not isinstance(aluno_atualizar, int):
                raise ValueError("O código do aluno deve ser um número.")

            novo_nome = input("Digite o novo nome do estudante: ")
            if not isinstance(novo_nome, str):
                raise ValueError("O nome do estudante deve ser uma string.")

            novo_cpf = input("Digite o novo CPF do estudante: ")
            if not isinstance(novo_cpf, str):
                raise ValueError("O CPF do estudante deve ser uma string.")

            novo_codigo = input("Digite o novo código do estudante: ")
            if not novo_codigo.isdigit():
                raise ValueError("O código do estudante deve ser um número.")
            aluno_atualizado = {
                "nome": novo_nome,
                "cpf": novo_cpf,
                "codigo": int(novo_codigo),
            }

            atualizar(
                aluno_atualizar,
                aluno_atualizado,
            )
        except ValueError as error:
            print(f"Erro ao atualizar o aluno: {error}")

    elif acao == "4":
        print(acoes.act4)
        codigo = input("Qual o código do aluno que deseja excluir: ")
        try:
            if not isinstance(int(codigo), int):
                raise ValueError("O código do aluno deve ser um número.")
            excluir(int(codigo))
            print("Aluno excluído com sucesso!")
        except ValueError as error:
            print(f"Erro ao excluir o aluno: {error}")
    else:
        print("Ação inválida. Por favor, escolha uma ação válida.")
