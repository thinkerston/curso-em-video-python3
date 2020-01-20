'''Crie um programa que tenha a função leiaint() que vai funcionar semelhante 
a funçaão input() do python, só que fazendo a validação para aceirar apenas 
um valor numérico'''

def leiaint(numero):
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

num = leiaint('Digite um numero: ')
print(f'Vc digitou {num}')