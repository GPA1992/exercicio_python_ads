import opcoes
import acoes
import geral
from gerenciar_dados import listar_todos, incluir
from gerenciar_estudantes import excluir, atualizar


def item_operacao(opt):
    if opt == "1":
        print(opcoes.opt1)
    if opt == "2":
        print(opcoes.opt2)
        print(geral.em_desenvolvimento)
        input("Pressione qualquer tecla para voltar pro menu principal...")
        rodar_aplicacao()
    if opt == "3":
        print(opcoes.opt3)
        print(geral.em_desenvolvimento)
        input("Pressione qualquer tecla para voltar pro menu principal...")
        rodar_aplicacao()
    if opt == "4":
        print(opcoes.opt4)
        print(geral.em_desenvolvimento)
        input("Pressione qualquer tecla para voltar pro menu principal...")
        rodar_aplicacao()
    if opt == "5":
        print(opcoes.opt5)
        print(geral.em_desenvolvimento)
        input("Pressione qualquer tecla para voltar pro menu principal...")
        rodar_aplicacao()
    if opt == "9":
        print(opcoes.opt9)


estudantes = []


def executar_acao_estudante():
    geral.menu_acoes()
    acao = input("Escolha uma ação desejada: ")

    if acao == "1":
        print(acoes.act1)
        estudante_nome = input("Digite o nome do novo estudante: ")
        estudante_cpf = input("Digite o CPF do novo estudante: ")
        incluir("alunos", {"nome": estudante_nome, "cpf": estudante_cpf})
        geral.mensagem_sucesso(estudante_nome)
        executar_acao_estudante()

    elif acao == "2":
        print(acoes.act2)
        print("Lista de Estudantes")
        listar_todos("alunos")
        print(geral.fim)
        executar_acao_estudante()

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
        executar_acao_estudante()

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
        executar_acao_estudante()

    elif acao == "9":
        rodar_aplicacao()

    else:
        print("Ação inválida. Por favor, escolha uma ação válida.")
        executar_acao_estudante()


def rodar_aplicacao():
    while True:
        geral.menu_principal()
        opt = input("Digite a opção desejada: ")

        if opt == "9":
            print("Finalizando aplicação..")
            exit()
        item_operacao(opt)
        executar_acao_estudante()


rodar_aplicacao()
