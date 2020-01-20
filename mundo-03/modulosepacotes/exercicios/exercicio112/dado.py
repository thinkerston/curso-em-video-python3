def leiaDinheiro(numero):
    isnumber = False
    valor = int(0)
    while True:
        number = str(input(numero))
        if number.isnumeric():
            valor = int(number)
            isnumber = True
        else:
            print('ERRO!!! Digite um numero valido')
        
        if isnumber == True:
            return(valor)

def leiaProcentagem(numero):
    isnumber = False
    valor = int(0)
    while True:
        number = str(input(numero))
        if number.isnumeric():
            valor = int(number)
            isnumber = True
        else:
            print('ERRO!!! Digite um numero valido')
        
        if isnumber == True:
            return(valor)