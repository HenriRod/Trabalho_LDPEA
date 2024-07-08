

print("Bem vindos a empresa do Henrique Rodrigues Da Luz")

# Iniciando uma lista de funcionarios em branco.
lista_funcionarios = []         # Iniciando uma lista de funcionarios vazia.
id_global = 4840748             # Variável id_global com meu RU.

def cadastrar_funcionario(id):              # Iniciando uma função def com intuito de cadrastrar id, nome, setor e salario.
    
    print(f"{60*"-"}\n{17*"-"}MENU CADRASTAR FUNCIONÁRIO{17*"-"}\nId do funcionário: {id_global}") #Menu com enfeites.
    id = id_global
    nome = input("Por favor entre com o nome do funcionário: ")                     #entrada de dados com inputs.
    setor = input("Por favor entre com o setor do funcionário: ")
    salario = float(input("Por favor entre com o salário do funcionário: "))
    
    
    funcionario = {             #guardando os dados obtidos com input.
        "ID": id,               #id já definido em uma variavel global com meu RU.
        "Nome": nome,
        "Setor": setor,
        "Salário": salario
    }
    lista_funcionarios.append(funcionario.copy())           #criando um dicionario com os dados obtidos acima utilizando o copy como pedido.

def consultar_funcionarios(): #criando a função de consultar funcionarios.
    while True:
        print("\nOpções de consulta:\n1. Consultar Todos os Funcionários \n2. Consultar Funcionarios por ID \n3. Consultar Funcionário por Setor \n4. Retornar ao Menu Anterior")
        opcao = input (">> ")   
        if opcao == "1":
            print("Funcionários cadastrados:")
            for funcionario in lista_funcionarios:          #verificando os funcionarios dentro do dicionario criado anteriormente.
                print(f"ID: {funcionario['ID']} \nNome: {funcionario['Nome']} \nSetor: {funcionario['Setor']} \nSalário: R${funcionario['Salário']:.2f}")
        elif opcao == "2":
            id_consulta = int(input("Digite o ID do funcionário: "))
            for funcionario in lista_funcionarios:
                if funcionario["ID"] == id_consulta:
                    print(f"ID: {funcionario['ID']} \nNome: {funcionario['Nome']} \nSetor: {funcionario['Setor']} \nSalário: R${funcionario['Salário']:.2f}")
                    break                   #executando o print e encerrando o laço caso de positivo.
            else:
                print("ID inválido.")       #Mostrando erro caso seja invalido o ID.
        elif opcao == "3":      #Verificando por setor
            setor_consulta = input("Digite o setor: ")  
            for funcionario in lista_funcionarios:
                if funcionario["Setor"].lower() == setor_consulta.lower():      #forçando a consulta a não diferenciar maiusculas e minusculas.
                    print(f"ID: {funcionario['ID']} \nNome: {funcionario['Nome']} \nSetor: {funcionario['Setor']} \nSalário: R${funcionario['Salário']:.2f}")
        elif opcao == "4":      #Função de retornar ao menu anterior caso seja necessario.
            return
        else:
            print("Opção inválida.")    #continuando o laço caso nenhuma das opção selecionadas sejam selecionadas.

def remover_funcionario():  #função de remover o funcionario com o Id fornecido.
    id_remover = int(input("Digite o ID do funcionário a ser removido: "))
    for funcionario in lista_funcionarios:      #Removendo da lista de funcionarios
        if funcionario["ID"] == id_remover:     #Filtrando com o ID.
            lista_funcionarios.remove(funcionario)      #Removendo
            print("Funcionário removido com sucesso.")
            break           #Encerrando com break caso as condições seja atendidas.
    else:
        print("ID inválido.")       #Caso digite um id invalido o laço se repete.

try:            #Usando try para rodar o codigo
    while True: 
        print(f"\n{28*"-"}Menu{28*"-"}\n1. Cadastrar Funcionário\n2. Consultar Funcionário\n3. Remover Funcionário\n4. Encerrar Programa")   #Menu com as opções a selecionar.
        
        opcao_menu = input("Escolha uma opção: ")   #Input para navegar nos menu raiz e fazer e redirecionamento.
        if opcao_menu == "1":
            cadastrar_funcionario(id_global)        #Cadrastando todos com meu RU.
        elif opcao_menu == "2":
            consultar_funcionarios()
        elif opcao_menu == "3":
            remover_funcionario()
        elif opcao_menu == "4":
            print("Encerrando o programa.")         #encerrar o loop caso já tenha feito tudo que queria.
            break
        else:
            print("Opção inválida.")
except Exception as e:                  #Qualquer do erro
    print(f"Erro: {e}")
except KeyboardInterrupt:               #caso queira finalizar abruptamente com CTRL+C
    print("\nOperação interrompida pelo usuário.")