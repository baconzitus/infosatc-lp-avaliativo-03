"""
6. Você foi escalado para desenvolver um sistema para um laboratório de doação de
sangue. Para ser um doador, a pessoa precisa atender os seguintes requisitos
básicos:
A. Ter entre 16 e 69 anos.
B. Mais de 50kg.
C. Ter dormido pelo menos 6h nas últimas 24horas;
O seu sistema precisa solicitar essas informações da pessoa, fazer as devidas
verificações e ao final mostrar se ela pode ser uma doadora ou não. Caso ela não
atenda algum dos requisitos, mostre qual requisito está fora do escopo.
"""
c_durmio=True
c_idade=True
c_peso=True

idade = int(input("insira a idade:"))
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
    if c_durmio==False:
        print("horas de sono insufientes ou exedidas")
    if c_idade==False:
        print("idade abaixo ou acima da aceita")
    if c_peso==False:
        print("peso abaixo do desejado")
else:
    print("\nveoce foi aceito para a doação")





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