#1
#Crie um programa que:
#Comece do número 1
#vá até o número 10
#Mostre todos os números no console

x = 0
while x <= 10:
    print(x)
    x += 1

#2
#Agora faz um programa que:
#Mostre apenas os números pares de 1 até 20

x = 2
while x <= 20:
    print(x)
    x += 2

#3
#Crie um programa que:
#Peça um número pro usuário
#Só pare quando o usuário digitar 0
#Enquanto isso, mostre: "Número digitado: X"

while True:
    num = float(input("Digite um número: "))
    if num == 0:
        print("ENCERRAR...")
        break

    print(f"Número digitado: {num}")

#4
#Crie um programa que:
#Some números digitados pelo usuário
#Continue pedindo números até o usuário digitar 0
#No final, mostre a soma total

soma = 0
num= float(input("Digite um número: "))

while num != 0:
    soma += num
    num = float(input("Digite um número: "))

print(f"A somatória total foi: {soma}")

#5
#Crie um programa que:
#Peça números ao usuário
#Pare quando digitar 0
#No final mostre:
#Quantos números foram digitados
#A soma total
#A média

soma = 0
numeros = 0

num = float(input("Digite um número: "))

while num != 0:
    soma += num
    numeros += 1

    num = float(input("Digite um número: "))

if numeros > 0:
    media = soma / numeros
else:
    media = 0

print(f"A soma total foi de: {soma}")
print(f"A média dos números digitados é de: {media}")

#6
#Crie um programa que:"
#Peça uma senha para o usuário
#A senha correta é: "python123"
#Enquanto errar, mostre: "Senha incorreta"
#Quando acertar, mostre: "Acesso liberado" e encerre

while True:
    senha = input("Digite sua senha: ")
    if senha == "python123":
        print("Acesso permitido")
        break
    else:
        print("Acesso negado")

#7
#Crie um programa que:
#Mostre a tabuada de um número escolhido pelo usuário
#A tabuada deve ir de 1 até 10
num  = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
