import opcoes
import acoes
import geral


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
        estudante = input("Digite o nome do novo estudante: ")
        estudantes.append(estudante)
        geral.mensagem_sucesso(estudante)
        executar_acao_estudante()

    if acao == "2":
        print(acoes.act2)
        if len(estudantes) == 0:
            print(geral.sem_estudantes_cadastrados)
            executar_acao_estudante()
        print(
            """Lista de Estudantes
              
"""
        )
        for indice, estudante in enumerate(estudantes):
            print(f"""{indice+1} - {estudante}""")
        print(geral.fim)
        executar_acao_estudante()

    if acao == "3":
        print(acoes.act3)
        print(geral.em_desenvolvimento)
        executar_acao_estudante()
    if acao == "4":
        print(acoes.act4)
        print(geral.em_desenvolvimento)
        executar_acao_estudante()
    if acao == "9":
        rodar_aplicacao()


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
