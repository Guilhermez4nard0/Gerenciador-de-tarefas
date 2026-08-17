tarefas = []
opcao = ""


while opcao != "4":
    print("=== Gerenciador de tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

    opcao = input("O que deseja fazer? ")


    if opcao == "1":
        tarefa = input("Digite sua tarefa: ")
        tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")


    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("Tarefas cadastradas:")
            for tarefa in tarefas:
                print(f"- {tarefa}")


        elif opcao == "3":
        numero = int(input("Digite o número da tarefa a ser removida: "))

            for i, t in enumerate(tarefas, start=1):

             if i == numero:
                tarefas.pop(i-1)
                print(f"Tarefa' {t} 'removida com sucesso!")
                break
        else:
            print("numero de tarefa inválido.")


    elif opcao == "4":
        print("Saindo...")

    else:
        print("Opção inválida.")
