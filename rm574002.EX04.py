print("Escolha o tipo de investimento:")
print("1. CDB")
print("2. LCI")
print("3. LCA")

tipo = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

if tipo == 1:
    valor = float(input("Digite o valor a ser resgatado: "))
    dias = int(input("Digite o número de dias que o valor permaneceu investido: "))

    if dias <= 180:
        aliquota = 22.5
    elif dias <= 360:
        aliquota = 20.0
    elif dias <= 720:
        aliquota = 17.5
    else:
        aliquota = 15.0

    ir = valor * (aliquota / 100)
    print(f"O valor do imposto de renda a ser pago é: R$ {ir:.2f}")

elif tipo == 2 or tipo == 3:
    valor = float(input("Digite o valor a ser resgatado: "))
    dias = int(input("Digite o número de dias que o valor permaneceu investido: "))
    print("Este investimento é isento de imposto de renda.")

else:
    print("Tipo de investimento inválido! Escolha 1, 2 ou 3.")