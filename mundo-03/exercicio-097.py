'''Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como paremetro e mostre a mensagem com tamanho adaptável'''

def Escreva(frase):
    size = int((len(frase) + 4))
    print('~' * size)
    print(frase.center(size, ' '))
    print('~' * (len(frase) + 4))
    
minhaFrase = str(input('Insira uma frase: '))
Escreva(minhaFrase)
