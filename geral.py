import menu


def menu_principal():
    print(
        f"""
--------------------- Menu Principal ---------------------
{menu.mn1[2]}
{menu.mn2[2]}
{menu.mn3[2]}
{menu.mn4[2]}
{menu.mn5[2]}
{menu.mnOut[2]}
"""
    )


sem_estudantes_cadastrados = """

Não há estudantes cadastrados.

"""


def mensagem_sucesso(nome_estudante):
    print(
        f"""--- Estudante {nome_estudante} adicionado(a) com sucesso! ---

* Escolha uma nova ação!
"""
    )


fim = """

--------------- Fim da lista ---------------

- Escolha uma nova ação!
"""


def menu_acoes():
    print(
        """
(1) Incluir
(2) Listar
(3) Atualizar
(4) Excluir
(9) Voltar ao menu principal
"""
    )


em_desenvolvimento = """

EM DESENVOLVIMENTO!

"""
