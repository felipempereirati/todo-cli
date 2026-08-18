"""
main.py
-------
Ponto de entrada do programa: mostra o menu, lê a opção do usuário
e chama as funções de tarefas.py. Toda a lógica de dados fica
separada em tarefas.py.

Autor: Felipe Mendes
"""

import tarefas


def exibir_menu():
    print("=== TO-DO LIST ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")


def listar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("📭 Nenhuma tarefa cadastrada ainda.\n")
        return

    print("\n--- SUAS TAREFAS ---")
    for tarefa in lista_tarefas:
        status = "✔️ " if tarefa["concluida"] else "⬜"
        print(f"{status} [{tarefa['id']}] {tarefa['titulo']}")
    print()


def pedir_id(mensagem):
    """Pede um ID ao usuário e valida se é um número. Retorna None se inválido."""
    try:
        return int(input(mensagem))
    except ValueError:
        print("⚠️  Digite um número válido.\n")
        return None


def main():
    lista_tarefas = tarefas.carregar_tarefas()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        print()

        if opcao == "1":
            titulo = input("Digite o título da tarefa: ").strip()
            if not titulo:
                print("⚠️  O título não pode ficar vazio.\n")
                continue
            tarefas.adicionar_tarefa(lista_tarefas, titulo)
            print(f"✅ Tarefa '{titulo}' adicionada com sucesso!\n")

        elif opcao == "2":
            listar_tarefas(lista_tarefas)

        elif opcao == "3":
            listar_tarefas(lista_tarefas)
            if not lista_tarefas:
                continue
            id_escolhido = pedir_id("Digite o ID da tarefa a concluir: ")
            if id_escolhido is None:
                continue
            if tarefas.concluir_tarefa(lista_tarefas, id_escolhido):
                print("🎉 Tarefa marcada como concluída!\n")
            else:
                print("⚠️  Tarefa não encontrada.\n")

        elif opcao == "4":
            listar_tarefas(lista_tarefas)
            if not lista_tarefas:
                continue
            id_escolhido = pedir_id("Digite o ID da tarefa a remover: ")
            if id_escolhido is None:
                continue
            if tarefas.remover_tarefa(lista_tarefas, id_escolhido):
                print("🗑️  Tarefa removida.\n")
            else:
                print("⚠️  Tarefa não encontrada.\n")

        elif opcao == "5":
            print("Até mais! 👋")
            break

        else:
            print("⚠️  Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
