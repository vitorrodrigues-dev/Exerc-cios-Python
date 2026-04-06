preco = float(input("Digite o preço do carro: "))

#Desconto à vista de 20% de desconto
preco_vista = preco * 0.80
print(f"O preço final á vista com desconto 20% é:{preco_vista}")

#Parcelado - loop de 6 a 60, de 6 em 6
parcelas = 6
acrescimo = 3

while parcelas <= 60:
    preco_parcelado = preco * (1 + acrescimo / 100)
    valor_parcela = preco_parcelado / parcelas

    print(f"O preço final parcelado em {parcelas} X é de R$ {preco_parcelado:.2f} com parcelas de R$ {valor_parcela:.2f}")

    parcelas += 6
    acrescimo += 3