valor_divida = float(input("Digite o valor da dívida: "))

contador = 1

while contador <= 5:
    if contador == 1:
        parcelas = 1
        juros = 0
    elif contador == 2:
        parcelas = 3
        juros = 10
    elif contador == 3:
        parcelas = 6
        juros = 15
    elif contador == 4:
        parcelas = 9
        juros = 20
    elif contador == 5:
        parcelas = 12
        juros = 25

    juros = valor_divida * (juros / 100)
    total = valor_divida + juros
    valor_parcela = total / parcelas

    print(f"Total: R${total:.2f} Juros:R${juros:.2f} Número de parcelas:{parcelas} Valor de PARCELA:R${valor_parcela:.2f}")

    contador += 1