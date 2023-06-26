from gerenciar_json import carregar_arquivo, salvar_arquivo
import acoes
import geral
from gerenciar_dados import listar_todos, incluir


def atualizar(codigo_professor, professor_atualizado):
    try:
        dados_totais = carregar_arquivo()
        professores = dados_totais["professores"]
        for professor in professores:
            if professor["codigo"] == int(codigo_professor):
                professor["nome"] = professor_atualizado["nome"]
                professor["cpf"] = professor_atualizado["cpf"]
                professor["codigo"] = professor_atualizado["codigo"]

        salvar_arquivo(dados_totais)
    except ValueError:
        print("O código do professor deve ser um número.")


def excluir(codigo_professor):
    try:
        dados_totais = carregar_arquivo()
        professores = dados_totais["professores"]

        for professor in professores:
            if professor["codigo"] == int(codigo_professor):
                professores.remove(professor)

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
        print("Lista de professores")
        listar_todos("professores")
        print(geral.fim)

    elif acao == "3":
        print(acoes.act3)
        professor_atualizar = input("Digite o código do professor: ")
        try:
            professor_atualizar = int(professor_atualizar)
            if not isinstance(professor_atualizar, int):
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
            professor_atualizado = {
                "nome": novo_nome,
                "cpf": novo_cpf,
                "codigo": int(novo_codigo),
            }

            atualizar(
                professor_atualizar,
                professor_atualizado,
            )
        except ValueError as error:
            print(f"Erro ao atualizar o professor: {error}")

    elif acao == "4":
        print(acoes.act4)
        codigo = input("Qual o código do professor que deseja excluir: ")
        try:
            if not isinstance(int(codigo), int):
                raise ValueError("O código do professor deve ser um número.")
            excluir(int(codigo))
            print("professor excluído com sucesso!")
        except ValueError as error:
            print(f"Erro ao excluir o professor: {error}")
    else:
        print("Ação inválida. Por favor, escolha uma ação válida.")
