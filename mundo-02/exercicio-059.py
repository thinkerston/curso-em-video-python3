# Paranid - Black Sabbath
'''crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] mostrar o maior valor
[4] inserir novos numeros
[5] sair do programa

seu programa deverá realizar a operação solicitada em cada caso'''
from time import sleep
primeiroValor = float(input('Insira o primeiro valor: '))
segundoValor = float(input('Insira o segundo valor: '))
sair = bool(False)

while sair == False:
    print('Qual operação deseja realizar')
    print('''[1] somar \n[2] multiplicar\n[3] mostrar o maior valor\n[4] inserir novos numeros\n[5] sair do programa''')
    operacao = int(input(': '))
    
    if operacao == 1:
        print(f'A soma entre {primeiroValor} e {segundoValor} é {primeiroValor + segundoValor}')
        pass
    elif operacao == 2:
        print(f'A multiplicação entre {primeiroValor} e {segundoValor} é {(primeiroValor * segundoValor)}')
        pass
    elif operacao == 3:
        if primeiroValor > segundoValor:
            print(f'o maior valor é: {primeiroValor}')
            pass
        else:
            print(f'o menor valor é: {segundoValor}')
            pass
        pass
    elif operacao == 4:
        primeiroValor = float(input('Insira o primeiro novo valor: '))
        segundoValor = float(input('insira o segundo novo valor: '))
        pass
    elif operacao == 5:
        print('estamos fechando o programa')
        sleep(3)
        sair = bool(True)
        print('hasta la vista baby... ')
        pass
    else:
        print('A operação que escolheu não pode ser realizada')
        pass