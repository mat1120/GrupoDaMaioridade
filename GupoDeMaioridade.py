from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(pessoa)))
    idade = ano_atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("No total,tivemos {} pessoas de maior".format(totmaior))
print("E tambem tivemos {} pessoas de menor".format(totmenor))