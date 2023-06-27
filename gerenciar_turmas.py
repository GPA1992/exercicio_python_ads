from gerenciar_json import carregar_arquivo, salvar_arquivo
import acoes
import geral
from gerenciar_dados import listar_todos, incluir


def atualizar(codigo_turma, turma_atualizada):
    try:
        dados_totais = carregar_arquivo()
        turmas = dados_totais["turmas"]
        for turma in turmas:
            if turma["codigo"] == int(codigo_turma):
                turma["codigo"] = turma_atualizada["codigo"]
                turma["codigo_professor"] = turma_atualizada["codigo_professor"]
                turma["codigo_disciplina"] = turma_atualizada["codigo_disciplina"]
        salvar_arquivo(dados_totais)
    except ValueError:
        print("O código da turma deve ser um número.")


def excluir(codigo_turma):
    try:
        dados_totais = carregar_arquivo()
        turmas = dados_totais["turmas"]
        for turma in turmas:
            if turma["codigo"] == int(codigo_turma):
                turmas.remove(turma)
        salvar_arquivo(dados_totais)
    except ValueError as error:
        print(error)
        return error


def executar_acao_turma(acao):
    geral.menu_acoes()
    if acao == "1":
        print(acoes.act1)
        while True:
            try:
                turma_codigo_professor = input(
                    "Digite o código de professor da nova turma: "
                )
                turma_codigo_disciplina = input(
                    "Digite o código da disciplina da nova turma: "
                )
                turma_codigo_professor = int(turma_codigo_professor)
                turma_codigo_disciplina = int(turma_codigo_disciplina)
                break
            except ValueError:
                print("Erro: Precisa ser números")

        incluir(
            "turmas",
            {
                "codigo_professor": turma_codigo_professor,
                "codigo_disciplina": turma_codigo_disciplina,
            },
        )
        print("Nova Turma Adicionada")

    elif acao == "2":
        print(acoes.act2)
        print("Lista de turmas")
        listar_todos("turmas")
        print(geral.fim)

    elif acao == "3":
        print(acoes.act3)
        turma_atualizar = input("Digite o código do turma: ")
        try:
            turma_atualizar = int(turma_atualizar)
            if not isinstance(turma_atualizar, int):
                raise ValueError("O código do turma deve ser um número.")

            novo_codigo_professor = input("Digite o novo código do professor: ")
            if not novo_codigo_professor.isdigit():
                raise ValueError("O código do professor deve ser um número.")

            novo_codigo_disciplina = input("Digite o novo código da disciplina: ")
            if not novo_codigo_disciplina.isdigit():
                raise ValueError("O código da disciplina deve ser um número.")

            novo_codigo_turma = input("Digite o novo código da turma: ")
            if not novo_codigo_disciplina.isdigit():
                raise ValueError("O código da disciplina deve ser um número.")

            turma_atualizada = {
                "codigo_professor": int(novo_codigo_professor),
                "codigo_disciplina": int(novo_codigo_disciplina),
                "codigo": int(novo_codigo_turma),
            }

            atualizar(
                turma_atualizar,
                turma_atualizada,
            )
        except ValueError as error:
            print(f"Erro ao atualizar o turma: {error}")

    elif acao == "4":
        print(acoes.act4)
        codigo = input("Qual o código do turma que deseja excluir: ")
        try:
            if not isinstance(int(codigo), int):
                raise ValueError("O código do turma deve ser um número.")
            excluir(int(codigo))
            print("turma excluído com sucesso!")
        except ValueError as error:
            print(f"Erro ao excluir o turma: {error}")
    else:
        print("Ação inválida. Por favor, escolha uma ação válida.")
