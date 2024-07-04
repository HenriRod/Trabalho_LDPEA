# Bem vindos à Fábrica de Camisetas do Bruno Kostiuk

def escolha_modelo():
    """
    Pergunta o modelo desejado e retorna o valor do modelo.
    Repete a pergunta se digitar uma opção diferente de: MCS/MLS/MCE/MLE.
    """
    while True:
        modelo = input("Escolha o modelo (MCS/MLS/MCE/MLE): ")
        if modelo in ["MCS", "MLS", "MCE", "MLE"]:
            if modelo == "MCS":
                return 1.80
            elif modelo == "MLS":
                return 2.10
            elif modelo == "MCE":
                return 2.90
            else:
                return 3.20
        else:
            print("Opção inválida. Tente novamente.")

def num_camisetas():
    """
    Pergunta o número de camisetas e retorna o número com desconto seguindo a regra do enunciado.
    Repete a pergunta se digitar um valor acima de 20000 ou valor não numérico.
    """
    while True:
        try:
            num = int(input("Digite o número de camisetas: "))
            if num < 20:
                return num
            elif 20 <= num < 200:
                return num * 0.95
            elif 200 <= num < 2000:
                return num * 0.93
            elif 2000 <= num <= 20000:
                return num * 0.88
            else:
                print("Quantidade de camisetas inválida. Tente novamente.")
        except ValueError:
            print("Valor não numérico. Tente novamente.")

def frete():
    """
    Pergunta pelo serviço adicional de frete e retorna o valor de apenas uma das opções de frete.
    Repete a pergunta se digitar uma opção diferente de: 1/2/0.
    """
    while True:
        opcao = input("Escolha o frete (1 - Transportadora, 2 - Sedex, 0 - Retirada na fábrica): ")
        if opcao in ["1", "2", "0"]:
            if opcao == "1":
                return 100
            elif opcao == "2":
                return 200
            else:
                return 0
        else:
            print("Opção inválida. Tente novamente.")

try:
    print("Bem vindos à Fábrica de Camisetas do Bruno Kostiuk")
    
    valor_modelo = escolha_modelo()
    quantidade_camisetas = num_camisetas()
    valor_frete = frete()
    
    total = (valor_modelo * quantidade_camisetas) + valor_frete
    print(f"Total a pagar: R$ {total:.2f}")
except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")
except Exception as e:
    print(f"Erro: {e}")