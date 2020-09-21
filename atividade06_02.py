"""
6.2. O laboratório gostou muito do seu serviço e pediu para que você adicione novos
recursos no sistema.
A. Após verificar se o usuário atende os requisitos, pergunte se ele gostaria de
se cadastrar no laboratório. Caso sim, armazene as seguintes informações
do usuário em uma sequência ou mapeamento (Escolha o tipo de dado que
mais se encaixa na sua opinião):
i. Nome Completo.
ii. CPF.
iii. Senha.
iv. Informação se ele está apto para doar sangue.
Se o usuário não desejar se cadastrar, apenas finalize o fluxo.
B. Faça o cadastro de pelo menos 5 pessoas.
C. Imprima todas as informações que foram armazenadas das 5 pessoas.
Obs: não esqueça dos padrões de commit e de fazer arquivo por arquivo.
Feat: quando novo arquivo
Fix: quando alteração ou ajuste
"""

nome = [ ]
cpf  = [ ]
senha =[ ]
doador=[ ]
c_durmio=True
c_idade=True
c_peso=True

while(True):
    idade = int(input("\ninsira a idade:"))
    peso  = int(input("insira o peso:"))
    durmio = int(input("insira a quantidade de horas durmidas nas ultimas 24horas:"))

    if idade<16 or idade>69:
        c_idade = False
    if peso<50:
        c_peso = False
    if durmio<6 or durmio>24:
        c_durmio = False

    if c_idade==False or c_durmio==False or c_peso==False:
        print("\nvoce não foi aceito porque:")
        hapto = False
        if c_durmio==False:
            print("horas de sono insufientes ou exedidas")
        if c_idade==False:
            print("idade abaixo ou acima da aceita")
        if c_peso==False:
            print("peso abaixo do desejado")
    else:
        print("\nvoce foi aceito para a doação")
        hapto=True   
    
    ##2 parte
    
    confirma = input("\nvoce gostaria de se registrar:s ou n: ")
    if confirma.lower()=="s":
        nome.append(input("nome completo:"))
        cpf.append (int((input("cpf:"))))
        senha.append(int(input("senha:")))
        if hapto==True:
            doador.append(True)
        else:
            doador.append(False)
        
        cont = input("deseja continuar cadastrando s ou n: ")
        if cont.lower()=="n":
            break
        elif cont.lower()=="s":
            pass
        else:
            print("comando n indentificado")
    elif confirma.lower()=="n":
        break
    else:
        print("comando n indentificado")


#n intendi a parte de cadastra 5 pessoas entao so coloquei elas ja que entrar os valores colocados durante a execucao  do programa sao perdidos    
#cadastrando outras 5 pessoas
    
for x in range(5):
    nome.append("nome exemplo")
    cpf.append(100) 
    senha.append(100) 
    doador.append(True)

geral = [nome,cpf,senha,doador]
print("\nLista de pessoas cadastradas aptas e nao aptas:")
for x in range(len(nome)):
    print("\nlugar:",x)
    print("nome:",geral[0][x])
    print("cpf:",geral[1][x])
    print("senha:",geral[2][x])
    print("pode doar:",geral[3][x])
        
    