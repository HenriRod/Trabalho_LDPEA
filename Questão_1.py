# Bem-vindos à loja do Bruno Kostiuk

# Input do valor do pedido e quantidade de parcelas
valorDoPedido = float(input("Digite o valor do pedido: "))
quantidadeParcelas = int(input("Digite a quantidade de parcelas: "))

# Cálculo dos juros conforme as condições
if quantidadeParcelas < 4:
    juros = 0
elif quantidadeParcelas < 6:
    juros = 0.04
elif quantidadeParcelas < 9:
    juros = 0.08
elif quantidadeParcelas < 13:
    juros = 0.16
else:
    juros = 0.32

# Cálculo do valor da parcela
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas

# Cálculo do valor total parcelado
valorTotalParcelado = valorDaParcela * quantidadeParcelas

# Exibição dos resultados
print(f"Valor da parcela: R$ {valorDaParcela:.2f}")
print(f"Valor total parcelado: R$ {valorTotalParcelado:.2f}")