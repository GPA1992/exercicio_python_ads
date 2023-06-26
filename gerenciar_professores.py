from gerenciar_json import carregar_arquivo, salvar_arquivo
import acoes
import geral
from gerenciar_dados import listar_todos, incluir


def atualizar(codigo_professor, professor_atualizado):
    try:
        dados_totais = carregar_arquivo()
        professores = dados_totais["professores"]
        for professore in professores:
            if professore["codigo"] == int(codigo_professor):
                professore["nome"] = professor_atualizado["nome"]
                professore["cpf"] = professor_atualizado["cpf"]
                professore["codigo"] = professor_atualizado["codigo"]

        salvar_arquivo(dados_totais)
    except ValueError:
        print("O código do professore deve ser um número.")


def excluir(codigo_professor):
    try:
        dados_totais = carregar_arquivo()
        professores = dados_totais["professores"]

        for professore in professores:
            if professore["codigo"] == int(codigo_professor):
                professores.remove(professore)

        salvar_arquivo(dados_totais)
    except ValueError as error:
        print(error)
        return error


def executar_acao_professor(acao):
    geral.menu_acoes()
    if acao == "1":
        print(acoes.act1)
        professor_nome = input("Digite o nome do novo professor: ")
        professor_cpf = input("Digite o CPF do novo professor: ")
        incluir("professores", {"nome": professor_nome, "cpf": professor_cpf})
        geral.mensagem_sucesso(professor_nome)

    elif acao == "2":
        print(acoes.act2)
        print("Lista de Professores")
        listar_todos("professores")
        print(geral.fim)

    elif acao == "3":
        print(acoes.act3)
        professore_atualizar = input("Digite o código do professor: ")
        try:
            professore_atualizar = int(professore_atualizar)
            if not isinstance(professore_atualizar, int):
                raise ValueError("O código do professor deve ser um número.")

            novo_nome = input("Digite o novo nome do professor: ")
            if not isinstance(novo_nome, str):
                raise ValueError("O nome do professor deve ser uma string.")

            novo_cpf = input("Digite o novo CPF do professor: ")
            if not isinstance(novo_cpf, str):
                raise ValueError("O CPF do professor deve ser uma string.")

            novo_codigo = input("Digite o novo código do professor: ")
            if not novo_codigo.isdigit():
                raise ValueError("O código do professor deve ser um número.")
            professore_atualizado = {
                "nome": novo_nome,
                "cpf": novo_cpf,
                "codigo": int(novo_codigo),
            }

            atualizar(
                professore_atualizar,
                professore_atualizado,
            )
        except ValueError as error:
            print(f"Erro ao atualizar o professore: {error}")

    elif acao == "4":
        print(acoes.act4)
        codigo = input("Qual o código do professore que deseja excluir: ")
        try:
            if not isinstance(int(codigo), int):
                raise ValueError("O código do professore deve ser um número.")
            excluir(int(codigo))
            print("professore excluído com sucesso!")
        except ValueError as error:
            print(f"Erro ao excluir o professore: {error}")
    else:
        print("Ação inválida. Por favor, escolha uma ação válida.")
