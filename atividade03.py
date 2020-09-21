mes = { 
    1:"janeiro",
    2:"fevereiro",
    3:"marco",
    4:"abril",
    5:"maio",
    6:"junho",
    7:"julho",
    8:"agosto",
    9:"setembro",
    10:"outubro",
    11:"novembro",
    12:"dezembro",
}
while(True):
    numero = (int(input("digite o numero do mes: ")))
    if numero in mes:
        print(mes[numero])
        break
    else:
        print("numero invalido")