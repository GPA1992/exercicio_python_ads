import opcoes
import geral
from gerenciar_estudantes import executar_acao_estudante
from gerenciar_professores import executar_acao_professor


def item_operacao(opt):
    if opt == "1":
        print(opcoes.opt1)
        return "alunos"
    if opt == "2":
        print(opcoes.opt2)
        return "professores"
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


def executar_acao(item):
    geral.menu_acoes()
    acao = input("Escolha uma ação desejada: ")
    if acao == "9":
        rodar_aplicacao()
    if item == "alunos":
        executar_acao_estudante(acao)
        executar_acao(item)
    if item == "professores":
        executar_acao_professor(acao)
        executar_acao(item)


def rodar_aplicacao():
    while True:
        geral.menu_principal()
        opt = input("Digite a opção desejada: ")

        if opt == "9":
            print("Finalizando aplicação..")
            exit()
        item = item_operacao(opt)
        executar_acao(item)


rodar_aplicacao()
