idadem=0 #nao funcionol sem declarar 
idadef=0
media=0
h=0
f=0

for x in range(3):
    while(True):
        sexo    = (str(input("insira o sexo da pessoa:")))
        idade   = (int(input("insira a idade da pessoa:")))
        if sexo.lower() == ("masculino"):
            idadem += idade
            media  += idade
            h += 1
            break
        elif sexo.lower() == ("feminino"):
            idadef += idade
            media  += idade
            f += 1
            break
        else:
            print("sexo invalido digite novamente")

if idadem>0: print("media de idade dos homens:",idadem/h)
if idadef>0:print("media de idade das mulheres",idadef/f)
if media>0:print("media de idade desse grupo:",media/(h+f))
