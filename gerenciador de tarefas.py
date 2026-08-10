print("=== Gerenciador de tarefas ===")
print("1. Adicionar tarefa")
print("2. ver tarefas")
print("3. Sair")

opcao = input("Oque deseja fazer? ")

if opcao == "1":
    tarefa = input("Digite sua tarefa: ")

    if opcao == "2":
        print("Tarefas:")
        print(f"- {tarefa}")

        if opcao == "3":
            print("Saindo do gerenciador de tarefas...")

            if opcao < 3:
                print("Opçao invalida.")