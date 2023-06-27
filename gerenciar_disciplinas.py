from gerenciar_json import carregar_arquivo, salvar_arquivo
import acoes
import geral
from gerenciar_dados import listar_todos, incluir


def atualizar(codigo_disciplina, disciplina_atualizado):
    try:
        dados_totais = carregar_arquivo()
        disciplinas = dados_totais["disciplinas"]
        for disciplina in disciplinas:
            if disciplina["codigo"] == int(codigo_disciplina):
                disciplina["nome"] = disciplina_atualizado["nome"]
                disciplina["codigo"] = int(disciplina_atualizado["codigo"])
        salvar_arquivo(dados_totais)
    except ValueError:
        print("O código da disciplina deve ser um número.")


def excluir(codigo_disciplina):
    try:
        dados_totais = carregar_arquivo()
        disciplinas = dados_totais["disciplinas"]
        for disciplina in disciplinas:
            if disciplina["codigo"] == int(codigo_disciplina):
                disciplinas.remove(disciplina)

        salvar_arquivo(dados_totais)
    except ValueError as error:
        print(error)
        return error


def executar_acao_disciplina(acao):
    geral.menu_acoes()
    if acao == "1":
        print(acoes.act1)
        disciplina_nome = input("Digite o nome da nova disciplina: ")
        incluir("disciplinas", {"nome": disciplina_nome})
        print(f"Disciplina {disciplina_nome} adicionada com sucesso")

    elif acao == "2":
        print(acoes.act2)
        print("Lista de disciplinas")
        listar_todos("disciplinas")
        print(geral.fim)

    elif acao == "3":
        print(acoes.act3)
        disciplina_atualizar = input("Digite o código do disciplina: ")
        try:
            disciplina_atualizar = int(disciplina_atualizar)
            if not isinstance(disciplina_atualizar, int):
                raise ValueError("O código do disciplina deve ser um número.")

            disciplina_nome = input("Digite o novo nome da disciplina: ")
            disciplina_codigo = input("Digite o novo codigo da disciplina: ")
            atualizar(
                disciplina_atualizar,
                {"nome": disciplina_nome, "codigo": disciplina_codigo},
            )
        except ValueError as error:
            print(f"Erro ao atualizar o disciplina: {error}")
    elif acao == "4":
        print(acoes.act4)
        codigo = input("Qual o código do disciplina que deseja excluir: ")
        try:
            if not isinstance(int(codigo), int):
                raise ValueError("O código do disciplina deve ser um número.")
            excluir(int(codigo))
            print("disciplina excluído com sucesso!")
        except ValueError as error:
            print(f"Erro ao excluir o disciplina: {error}")
    else:
        print("Ação inválida. Por favor, escolha uma ação válida.")
