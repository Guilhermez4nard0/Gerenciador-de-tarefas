tarefas = []
opcao = ""


while opcao != "3":
    print("=== Gerenciador de tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Sair")

    opcao = input("O que deseja fazer? ")

    
    if opcao == "1":
        tarefa = input("Digite sua tarefa: ")
        tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")

    
    elif opcao == "2":
        print("Tarefas:")
        for tarefa in tarefas:
            print(f"- {tarefa}")

    
    elif opcao == "3":
        print("Saindo...")

    
    else:
        print("Opção inválida.")
        
