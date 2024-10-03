# Definição de Dados
tarefas = []  # Lista para armazenar as tarefas

def mostrar_menu():
    print("""
    Gerenciador de Tarefas
    1. Adicionar tarefa
    2. Listar tarefas
    3. Marcar tarefa como concluída
    4. Exibir tarefas por prioridade
    5. Exibir tarefas por categoria
    6. Sair""")

def adicionar_tarefa():
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    prioridade = input("Prioridade (alta, média, baixa): ")
    categoria = input("Categoria: ")
    
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, tarefa in enumerate(tarefas):
        status = "✔️" if tarefa['concluida'] else "❌"
        print(f"{i + 1}. {tarefa['nome']} - {status} | Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']}")

def marcar_tarefa_concluida():
    listar_tarefas()
    try:
        indice = int(input("Escolha o número da tarefa para marcar como concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]['concluida'] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Tarefa não encontrada.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

def exibir_por_prioridade():
    prioridade = input("Digite a prioridade (alta, média, baixa): ")
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['prioridade'] == prioridade]
    
    if not tarefas_filtradas:
        print("Nenhuma tarefa encontrada com essa prioridade.")
        return

    for tarefa in tarefas_filtradas:
        status = "✔️" if tarefa['concluida'] else "❌"
        print(f"{tarefa['nome']} - {status} | Categoria: {tarefa['categoria']}")

def exibir_por_categoria():
    categoria = input("Digite a categoria: ")
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['categoria'] == categoria]
    
    if not tarefas_filtradas:
        print("Nenhuma tarefa encontrada nessa categoria.")
        return

    for tarefa in tarefas_filtradas:
        status = "✔️" if tarefa['concluida'] else "❌"
        print(f"{tarefa['nome']} - {status} | Prioridade: {tarefa['prioridade']}")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            marcar_tarefa_concluida()
        elif opcao == '4':
            exibir_por_prioridade()
        elif opcao == '5':
            exibir_por_categoria()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
