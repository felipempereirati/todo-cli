"""
tarefas.py
----------
Responsável por toda a lógica de dados: carregar, salvar,
adicionar, concluir e remover tarefas.
Não lida com input()/print() de menu — isso fica em main.py.
"""

import json
import os

ARQUIVO_TAREFAS = "tarefas.json"


def carregar_tarefas():
    """Lê o arquivo JSON com as tarefas salvas. Retorna [] se não existir."""
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []

    with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo JSON."""
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


def gerar_novo_id(tarefas):
    """Gera o próximo ID disponível (maior ID + 1, ou 1 se lista vazia)."""
    if not tarefas:
        return 1
    return max(tarefa["id"] for tarefa in tarefas) + 1


def adicionar_tarefa(tarefas, titulo):
    """Cria e adiciona uma nova tarefa à lista. Retorna a tarefa criada."""
    nova_tarefa = {
        "id": gerar_novo_id(tarefas),
        "titulo": titulo,
        "concluida": False,
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    return nova_tarefa


def concluir_tarefa(tarefas, id_escolhido):
    """Marca a tarefa com o ID informado como concluída. Retorna True se encontrou."""
    for tarefa in tarefas:
        if tarefa["id"] == id_escolhido:
            tarefa["concluida"] = True
            salvar_tarefas(tarefas)
            return True
    return False


def remover_tarefa(tarefas, id_escolhido):
    """Remove a tarefa com o ID informado. Retorna True se encontrou e removeu."""
    for tarefa in tarefas:
        if tarefa["id"] == id_escolhido:
            tarefas.remove(tarefa)
            salvar_tarefas(tarefas)
            return True
    return False
