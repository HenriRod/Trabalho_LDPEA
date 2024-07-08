#Primeiro print com a exigencia do nome completo
print("Bem vindos à Fábrica de Camisetas do Henrique Rodrigues Da Luz")

def escolha_modelo():       #Aqui tenho a função de escolha entre as camisas e definindo seus respectivos valores.  
    while True:
        modelo = input("Entre com o modelo desejado\nMCS - Manga Curta Simples\nMLS - Manga Longa Simples\nMCE - manga Curta Com Estampa\nMLE - Manga Longa Com Estampa\n>> ")
        if modelo in ["MCS", "MLS", "MCE", "MLE"]:          #função usada como filtro de input com todos os 4 modelos exigidos.
            if modelo == "MCS":
                return 1.80                     #returns colocados com o valor de acordo com o modelo de camisa.
            elif modelo == "MLS":
                return 2.10                                     
            elif modelo == "MCE":
                return 2.90
            else:           #Resto = MLE
                return 3.20
        else:
            print("Escolha inválida, entre com o modelo novamente.\n ")    #retornando o loop caso o input seja invalido.
              
def num_camisetas(): #DEF para filtrar a quantidade de produtos e dar um valor de porcentual de desconto pré-fixado.
    while True:
        try:
            qtd = int(input("Entre com o número de camisetas: "))
            if qtd < 20:
                return qtd                  #usando return como solicitado
            elif 20 <= qtd < 200:
                return qtd * 0.95        #descontos com base no número de camisetas.
            elif 200 <= qtd < 2000:
                return qtd * 0.93       #Abreviei a porcentagem aqui pois estava dando conflitos no resultado final usando dessa forma: (x/100), ele imprimia o x...
            elif 2000 <= qtd <= 20000:
                return qtd * 0.88
            else:
                print("Não aceitamos tantas camisetas de uma vez \nPor favor, entre como número de camisetas novamente.\n ")
        except ValueError:          #usando except para filtrar caracteres não numéricos
            print("Digite um numero entre 1 e 20000, caracteres especiais não são aceitos! Tente novamente.")

def frete():        #DEF para selecionar o valor do frete. com loop para evitar sair das opções pré-selecionadas.
    while True:
        opcoes = input("\nEscolha o tipo de frete: \n1 - Transportadora - R$ 100.00\n2 - Sedex - R$ 200.00 \n0 - Retirada na fábrica - R$ 0.00 \n>> ")
        if opcoes in ["1", "2", "0"]:       #criando as opções que definira a taxa ou não do frete.
            if opcoes == "1":
                return 100.00               #return usado para definir os valores de cada opção.
            elif opcoes == "2":
                return 200.00
            else:
                return 0.00
        else:
            print("Opção inválida. Tente novamente.")       #reiniciando o loop caso o número digitado seja diferente de 1/2/0.

try:        #implementando o calculo do total a pagar fora dos defs.
    valor_modelo = escolha_modelo()
    quantidade_camisetas = num_camisetas()
    valor_frete = frete()
    
    total = (valor_modelo * quantidade_camisetas) + valor_frete 
    print(f"Total: R$ {total:.2f} (Modelo: {valor_modelo} * Quantidade(com desconto): {quantidade_camisetas} + Frete: {valor_frete})")
except Exception as e:
    print(f"Erro: {e}")             #print do erro
except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")      #print caso o usuário cancele a run abruptamente do console usando ctrl+c.