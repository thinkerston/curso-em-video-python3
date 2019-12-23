'''Faça um programa que leia um numero inteiro e diga se ele é primo'''

numero = int(input('Insira um numero para verificar se é primo: '))
primo = bool(False)
for i in range(1, numero + 1):
    if (numero % i == 0):
        if (i != 1) and (i != numero):
            primo = False
            break
        else:
            primo = True
            
if primo == False:
    print(f'O Numero {numero} NÃO É PRIMO')
else:
    print(f'o numero {numero}  É PRIMO')