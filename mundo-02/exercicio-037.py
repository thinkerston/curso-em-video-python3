'''Escreva um programa que leia um numero inteiro qualquer e peça para o
usuario escolhar qual será a base de conversão
1- para binário
2- para octal
3- hexadecimal'''

converter = int(input('insira um numero inteiro deseja converter: '))
print(' ')
print('1- para binário')
print('2- para octal')
print('3- hexadecimal')

escolha = int(input('Escolha para converter: '))

if escolha == 1: #Binário
    binario = bin(converter).split('b')[-1]
    print(f'O numero {converter} em binario é {binario}')
    pass
elif escolha == 2: #octal
    octal = oct(converter).split('o')[-1]
    print(f'O numero {converter} em octal é {octal}')
    pass
elif escolha == 3: #hexadecimal
    hexadecimal = hex(converter).split('x')[-1]
    print(f'O numero {converter} em hexadecimal é {hexadecimal}') 
    pass
else:
    print('o numero escolhido não faz parte')
    pass