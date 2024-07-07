#Primeiro print com a exigencia do nome completo
print("Bem vindos à Fábrica de Camisetas do Henrique Rodrigues Da Luz")

def escolha_modelo():       #Aqui tenho a funcão de escolha entre as camisas e definindo seus respectivos valores.  
    while True:
        modelo = input("Entre com o modelo desejado\nMCS - Manga Curta Simples\nMLS - Manga Longa Simples\nMCE - manga Curta Com Estampa\nMLE - Manga Longa Com Estampa\n>> ")
        if modelo in ["MCS", "MLS", "MCE", "MLE"]:
            if modelo == "MCS":
                return 1.80
            elif modelo == "MLS":
                return 2.10
            elif modelo == "MCE":
                return 2.90
            else:           #Resto = MLE
                return 3.20
        else:
            print("Escolha inválida, entre com o modelo novamente.")       #encerando o laço

def num_camisetas(): #DEF para filtrar a quantidade em relação ao porcentual de desconto.
    """
    Pergunta o número de camisetas e retorna o número com desconto seguindo a regra do enunciado.
    Repete a pergunta se digitar um valor acima de 20000 ou valor não numérico.
    """
    while True:
        try:
            qtd = int(input("Entre com o número de camisetas: "))
            if qtd < 20:
                return qtd
            elif 20 <= qtd < 200:
                return qtd * (5/100)
            elif 200 <= qtd < 2000:
                return qtd * (7/100)
            elif 2000 <= qtd <= 20000:
                return qtd * (12/100)
            else:
                print("Não aceitamos tantas camisetas de uma vez \n Por favor, entre como número de camisetas novamente.")
        except ValueError:
            print("Digite um numero entre 1 e 20000, caracteres especiais não são aceitos! Tente novamente.")

def frete():        #DEF para selecionar o valor do frete. com loop para evitar sair das opções pre-selecionadas.
    while True:
        opcoes = input("Escolha o tipo de frete: \n1 - Transportadora - R$ 100.00\n2 - Sedex - R$ 200.00 \n 0 - Retirada na fábrica - R$ 0.00 ")
        if opcoes in ["1", "2", "0"]:
            if opcoes == "1":
                return 100.00
            elif opcoes == "2":
                return 200.00
            else:
                return 0.00
        else:
            print("Opção inválida. Tente novamente.")

try:        #Definindo nome de String para as funções defs para realizar o calculo das variaveis 
    valor_modelo = escolha_modelo()
    quantidade_camisetas = num_camisetas()
    valor_frete = frete()
    
    total = (valor_modelo * quantidade_camisetas) + valor_frete 
    print(f"Total a pagar: R$ {total:.2f}")
except Exception as e:
    print(f"Erro: {e}")
except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")