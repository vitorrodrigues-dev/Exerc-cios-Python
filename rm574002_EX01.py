num_colaboradores = int(input("Informe o número de colaboradores: "))

seg = 0
ter = 0
qua = 0
qui = 0
sex = 0

for i in range(num_colaboradores):
    dia = input("Informe o dia da sua preferência (segunda-feira, terça-feira, quarta-feira,quinta-feira, sexta-feira): ")

    if dia == "segunda-feira":
        seg += 1
    elif dia == "terça-feira":
        ter += 1
    elif dia == "quarta-feira":
        qua += 1
    elif dia == "quinta-feira":
        qui += 1
    elif dia == "sexta-feira":
        sex += 1

maior = seg

if ter > maior:
    maior = ter
if qua > maior:
    maior = qua
if qui > maior:
    maior = qui
if sex > maior:
    maior = sex

#Verificação caso der empate e exibição do resultado
empate = False

if seg == maior and ter == maior:
    empate = True
elif seg == maior and qua == maior:
    empate = True
elif seg == maior and qui == maior:
    empate = True
elif seg == maior and sex == maior:
    empate = True
elif ter == maior and qua == maior:
    empate = True
elif ter == maior and qui == maior:
    empate = True
elif ter == maior and sex == maior:
    empate = True
elif qua == maior and qui == maior:
    empate = True
elif qua == maior and sex == maior:
    empate = True
elif qui == maior and sex == maior:
    empate = True

if empate:
    print("Houve empate entre os dias mais votados!")
elif maior == seg:
    print("O dia escolhido pelos colaboradores é: segunda-feira")
elif maior == ter:
    print("O dia escolhido pelos colaboradores é: terça-feira")
elif maior == qua:
    print("O dia escolhido pelos colaboradores é: quarta-feira")
elif maior == qui:
    print("O dia escolhido pelos colaboradores é: quinta-feira")
elif maior == sex:
    print("O dia escolhido pelos colaboradores é: sexta-feira")


