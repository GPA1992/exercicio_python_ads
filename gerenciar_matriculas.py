from gerenciar_json import carregar_arquivo, salvar_arquivo
import acoes
import geral
from gerenciar_dados import listar_todos, incluir


def atualizar(codigo_estudante, matricula_atualizado):
    try:
        dados_totais = carregar_arquivo()
        matriculas = dados_totais["matriculas"]
        for matricula in matriculas:
            if matricula["codigo_estudante"] == int(codigo_estudante):
                matricula["codigo_turma"] = int(matricula_atualizado["codigo_turma"])
                matricula["codigo_estudante"] = int(
                    matricula_atualizado["codigo_estudante"]
                )
        salvar_arquivo(dados_totais)
    except ValueError:
        print("O código da matricula deve ser um número.")


def excluir(codigo_estudante):
    try:
        dados_totais = carregar_arquivo()
        matriculas = dados_totais["matriculas"]
        for matricula in matriculas:
            if matricula["codigo_estudante"] == int(codigo_estudante):
                matriculas.remove(matricula)
        salvar_arquivo(dados_totais)
    except ValueError as error:
        print(error)
        return error


def executar_acao_matricula(acao):
    geral.menu_acoes()
    if acao == "1":
        print(acoes.act1)
        codigo_turma = input("Digite o codigo de turma da nova matricula: ")
        codigo_estudante = input("Digite o codigo do estudante da nova matricula: ")
        incluir(
            "matriculas",
            {
                "codigo_turma": int(codigo_turma),
                "codigo_estudante": int(codigo_estudante),
            },
        )
        print("Nova matricula feita com sucesso")

    elif acao == "2":
        print(acoes.act2)
        print("Lista de matriculas")
        listar_todos("matriculas")
        print(geral.fim)

    elif acao == "3":
        print(acoes.act3)
        matricula_atualizar = input("Digite o código do estudante: ")
        matricula_atualizar = int(matricula_atualizar)
        codigo_turma = input("Digite o codigo de turma da nova matricula: ")
        codigo_estudante = input("Digite o codigo do estudante da nova matricula: ")
        matricula_atualizado = {
            "codigo_turma": int(codigo_turma),
            "codigo_estudante": int(codigo_estudante),
        }
        atualizar(
            matricula_atualizar,
            matricula_atualizado,
        )
        print("Matricula Atualizada com sucesso")
    elif acao == "4":
        print(acoes.act4)
        codigo = input("Qual o código do matricula que deseja excluir: ")
        try:
            if not isinstance(int(codigo), int):
                raise ValueError("O código do matricula deve ser um número.")
            excluir(int(codigo))
            print("matricula excluído com sucesso!")
        except ValueError as error:
            print(f"Erro ao excluir o matricula: {error}")
    else:
        print("Ação inválida. Por favor, escolha uma ação válida.")
