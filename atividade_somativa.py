import opcoes
import geral
from gerenciar_estudantes import executar_acao_estudante
from gerenciar_professores import executar_acao_professor
from gerenciar_disciplinas import executar_acao_disciplina
from gerenciar_turmas import executar_acao_turma
from gerenciar_matriculas import executar_acao_matricula


def item_operacao(opt):
    if opt == "1":
        print(opcoes.opt1)
        return "alunos"
    if opt == "2":
        print(opcoes.opt2)
        return "professores"
    if opt == "3":
        print(opcoes.opt3)
        return "disciplinas"
    if opt == "4":
        print(opcoes.opt4)
        return "turmas"
    if opt == "5":
        print(opcoes.opt5)
        return "matriculas"
    if opt == "9":
        print(opcoes.opt9)


estudantes = []


def executar_acao(item):
    geral.menu_acoes()
    acao = input("Escolha uma ação desejada: ")
    if acao == "9":
        rodar_aplicacao()
    elif item == "alunos":
        executar_acao_estudante(acao)
    elif item == "professores":
        executar_acao_professor(acao)
    elif item == "disciplinas":
        executar_acao_disciplina(acao)
    elif item == "turmas":
        executar_acao_turma(acao)
    elif item == "matriculas":
        executar_acao_matricula(acao)
    else:
        print("Item inválido.")
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
