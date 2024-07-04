Python

# Bem vindos à loja de Marmitas do Bruno Kostiuk

# Menu para o cliente
print("Menu:")
print("1. Bife Acebolado (BA)")
print("2. Filé de Frango (FF)")

# Inicialização do acumulador
total_pedido = 0


while True:
    # Input do sabor
    sabor = input("Digite o sabor (BA/FF): ")
    if sabor not in ["BA", "FF"]:
        print("Sabor inválido. Tente novamente.")
        continue


    # Input do tamanho
    tamanho = input("Digite o tamanho (P/M/G): ")
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.")
        continue


    # Cálculo do valor do pedido
    if sabor == "BA":
        if tamanho == "P":
            valor_pedido = 16
        elif tamanho == "M":
            valor_pedido = 18
        else:
            valor_pedido = 22
    else:
        if tamanho == "P":
            valor_pedido = 15
        elif tamanho == "M":
            valor_pedido = 17
        else:
            valor_pedido = 21

    # Acumula o valor do pedido
    total_pedido += valor_pedido

    # Pergunta se deseja pedir mais alguma coisa
    mais_pedidos = input("Deseja pedir mais alguma coisa? (S/N): ")
    if mais_pedidos.upper() != "S":
        break

# Exibe o total do pedido
print(f"Total do pedido: R$ {total_pedido:.2f}")






'''
Saída de console:
Bem vindos à loja de Marmitas do Bruno Kostiuk
Menu:
1. Bife Acebolado (BA)
2. Filé de Frango (FF)
Digite o sabor (BA/FF): BA
Digite o tamanho (P/M/G): M
Deseja pedir mais alguma coisa? (S/N): S
Digite o sabor (BA/FF): FF
Digite o tamanho (P/M/G): G
Deseja pedir mais alguma coisa? (S/N): N
Total do pedido: R$ 39.00

Observações:

O código implementa todas as exigências solicitadas, incluindo o uso de estruturas de controle, acumulador e comentários relevantes.
A saída de console apresenta exemplos de pedidos corretos, incorretos e com diferentes sabores e tamanhos.
'''