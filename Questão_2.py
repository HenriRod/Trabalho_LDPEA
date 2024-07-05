# Prints da primeira exigência com nome completo e um menu.
print("-----Bem vindos a loja de Marmitas do Henrique Rodrigues Da Luz-----")
print(f"{30*"-"}Cardápio{30*"-"}\n{68*"-"}")
print("----|  Tamanho  |  Bife Acebolado(BA)  |  Filé de Frango(FF)   |----")
print("----|     P     |       R$ 16.00       |      R$ 15.00         |----")
print("----|     M     |       R$ 18.00       |      R$ 17.00         |----")
print(f"----|     G     |       R$ 22.00       |      R$ 21.00         |----\n{68*"-"}")

# código usado para saber o tamanho da primeira string e fazer a base do cardápio.
'''
texto_base = "-----Bem vindos a loja de Marmitas do Henrique Rodrigues Da Luz-----"
tamanho = len(texto_base)
print(f"O tamanho da string é: {tamanho}")
'''

# Iniciando uma variável acumuladora para não dar erro quando for somar. 
total_do_pedido = 0

while True:
    # Input do sabor para fazer a validação do BA ou FF.
    sabor = input("Entre com o sabor desejado (BA/FF): ")
    if sabor not in ["BA", "FF"]:
        print("Sabor inválido. Tente novamente.")
        continue

    # Input do tamanho com a validação dos dados digitados P,M,G.
    tamanho = input("Entre com o tamanho desejado (P/M/G): ")
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.")
        continue

    # Cálculo do valor do pedido usando if, elif e else para cada um dos sabores e com indentações.
    if sabor == "BA":
        if tamanho == "P":
            valor_do_pedido = 16
            print(f"Você pediu um Bife Acebolado no tamanho P: R$ {valor_do_pedido:.2f}")
        elif tamanho == "M":
            valor_do_pedido = 18
            print(f"Você pediu um Bife Acebolado no tamanho M: R$ {valor_do_pedido:.2f}")
        else:
            valor_do_pedido = 22
            print(f"Você pediu um Bife Acebolado no tamanho G: R$ {valor_do_pedido:.2f}")
    else:
        if tamanho == "P":
            valor_do_pedido = 15
            print(f"Você pediu um Filé de Frango no tamanho P: R$ {valor_do_pedido:.2f}")
        elif tamanho == "M":
            valor_do_pedido = 17
            print(f"Você pediu um Filé de Frango no tamanho M: R$ {valor_do_pedido:.2f}")
        else:
            valor_do_pedido = 21
            print(f"Você pediu um Filé de Frango no tamanho G: R$ {valor_do_pedido:.2f}")

    # Acumulando o valor do pedido antes de resetar o loop.
    total_do_pedido += valor_do_pedido

    # Perguntando se o cliente quer pedir mais alguma coisa antes de finalizar o loop, ou voltar ao inicio da mesma para acumular mais itens no cardápio.
    mais_pedidos = input("Deseja mais alguma coisa? (S/N): ")
    if mais_pedidos.upper() != "S":
        break

# print final com o valor total do pedido a ser pago.
print(f"Valor total a ser pago: R$ {total_do_pedido:.2f}")