#1
#Crie um programa que:
#peça um número ao usuário
#verifique se esse número é par ou ímpar
#mostre uma mensagem dizendo o resultado

numero = int(input("Digite um número inteiro e veja se é impar ou par:"))

if numero % 2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é impar")

#2
#Crie um programa que:
#peça a idade da pessoa
#verifique:
#se idade < 18 → "Menor de idade"
#se idade entre 18 e 59 → "Adulto"
#se idade ≥ 60 → "Idoso"

idade = int(input("Digite sua idade(em anos): "))
if idade < 18:
    print("Menor de idade")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")

#3
#Crie um programa que:
#peça usuário
#peça senha
#E verifique:
#se usuário for "admin" E senha for "1234" → mostrar "Acesso permitido"
#senão → mostrar "Acesso negado"

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == 1234:
    print("Acesso permitido")
else:
    print("Acesso negado")

#4
#Crie um programa que:
#peça a idade
#peça se a pessoa tem carteira de motorista (sim ou não)
#E verifique:
#se idade ≥ 18 E tiver carteira → "Pode dirigir"
#senão → "Não pode dirigir"

idade = int(input("Digite sua idade: "))
carteira_dirigir = input("Você tem carteira de dirigir(sim ou não): ").lower().strip()
if idade < 18:
    print("Menor de idade, não pode dirigir")
elif carteira_dirigir != "sim":
   print("Precisa tirar a carteira de direção")
else:
    print("Pode dirigir")


#5
#Simular uma compra com regras reais
#O programa deve:
#Pedir o nome do cliente
#Pedir o valor da compra
#Perguntar se é cliente VIP (sim ou não)
#Se for VIP e compra ≥ 100 → 20% de desconto
#Se NÃO for VIP e compra ≥ 100 → 10% de desconto
#Caso contrário → sem desconto

nome = input("Digite seu nome: ")
valor_compra = float(input("Digite o valor da compra: "))
cliente_vip = input("Você é um cliente VIP(sim ou não): ").lower().strip()

if cliente_vip in ['sim', 'yes', 's'] and valor_compra >= 100:
    desconto = valor_compra * 0.20
elif valor_compra >= 100:
    desconto = valor_compra * 0.10
else:
    desconto = 0

valor_final = valor_compra - desconto


print(f"Cliente: {nome}")
print(f"Valor original: {valor_compra}")
print(f"Desconto: {desconto}")
print(f"Valor final: {valor_final}")