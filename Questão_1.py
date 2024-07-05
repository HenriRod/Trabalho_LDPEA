# print da primeira condição com o nome completo.     
print("Bem-vindos a loja do Henrique Rodrigues Da Luz")

# Input para obter do valor do pedido.          
valor_do_pedido = float(input ("Entre com o valor do pedido: "))
# Input para obter os dados da parcela.
quantidade_de_parcelas = int(input("Entre com a quantidade de parcelas: "))

# Estrutura com if, elif, else. para o cálculo dos juros de acordo com as parcelas!    
if quantidade_de_parcelas < 4:          
    juros = 0 / 100
elif quantidade_de_parcelas >= 4 and quantidade_de_parcelas < 6:    # aqui poderia deixar o codigo mais clean apenas retirando a primeira variável e o >= pois o if acima confirma isso. 
    juros = 4 / 100
elif quantidade_de_parcelas >= 6 and quantidade_de_parcelas < 9:    # mas deixei como foi solicitado com "igual ou maior que" e "menor que"...
    juros = 8 / 100
elif quantidade_de_parcelas >= 9 and quantidade_de_parcelas < 13:   
    juros = 16 / 100
else:
    juros = 32 / 100

# Cálculo do valor da parcela.
valor_da_parcela = ( valor_do_pedido * ( 1 + juros ) ) / quantidade_de_parcelas

# Cálculo do valor total parcelado.
valor_total_parcelado = valor_da_parcela * quantidade_de_parcelas

# Prints finais com os dois resultados: valor da parcela e valor total parcelado.
print(f"O valor das parcelas é de: R$ { valor_da_parcela:.2f}")
print(f"O valor Total Parcelado é de: R$ {valor_total_parcelado:.2f}")