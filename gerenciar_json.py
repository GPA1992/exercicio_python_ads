import json


def carregar_arquivo():
    with open("data.json", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return dados


def salvar_arquivo(data):
    with open("data.json", "w", encoding="utf-8") as arquivo:
        json.dump(data, arquivo)
