# Bem vindos à empresa do Bruno Kostiuk

# Lista de funcionários (cada funcionário é um dicionário)
lista_funcionarios = []
# Variável global para o ID
id_global = 2023000

def cadastrar_funcionario(id):
    """
    Pergunta nome, setor e salário do funcionário.
    Armazena os dados em um dicionário e adiciona à lista de funcionários.
    """
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    
    funcionario = {
        "ID": id,
        "Nome": nome,
        "Setor": setor,
        "Salário": salario
    }
    
    lista_funcionarios.append(funcionario.copy())

def consultar_funcionarios():
    """
    Consulta funcionários com base na opção escolhida pelo usuário.
    """
    while True:
        print("\nOpções de consulta:")
        print("1. Consultar Todos")
        print("2. Consultar por ID")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\nFuncionários cadastrados:")
            for funcionario in lista_funcionarios:
                print(funcionario)
        elif opcao == "2":
            id_consulta = int(input("Digite o ID do funcionário: "))
            for funcionario in lista_funcionarios:
                if funcionario["ID"] == id_consulta:
                    print(funcionario)
                    break
            else:
                print("ID inválido.")
        elif opcao == "3":
            setor_consulta = input("Digite o setor: ")
            for funcionario in lista_funcionarios:
                if funcionario["Setor"].lower() == setor_consulta.lower():
                    print(funcionario)
        elif opcao == "4":
            return
        else:
            print("Opção inválida.")

def remover_funcionario():
    """
    Remove um funcionário da lista com base no ID fornecido.
    """
    id_remover = int(input("Digite o ID do funcionário a ser removido: "))
    for funcionario in lista_funcionarios:
        if funcionario["ID"] == id_remover:
            lista_funcionarios.remove(funcionario)
            print("Funcionário removido com sucesso.")
            break
    else:
        print("ID inválido.")

try:
    print("Bem vindos à empresa do Bruno Kostiuk")
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar Funcionário")
        print("2. Consultar Funcionário")
        print("3. Remover Funcionário")
        print("4. Encerrar Programa")
        
        opcao_menu = input("Escolha uma opção: ")
        
        if opcao_menu == "1":
            id_global += 1
            cadastrar_funcionario(id_global)
        elif opcao_menu == "2":
            consultar_funcionarios()
        elif opcao_menu == "3":
            remover_funcionario()
        elif opcao_menu == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")
except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")
except Exception as e:
    print(f"Erro: {e}")
