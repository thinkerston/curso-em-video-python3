'''Escreva um programa que faça o computador 'pensar' em um numero inteiro
ente 0 e 5 e peça para o usuário tentar descobrir qual foi o numero
escolhido  pelo computador. O progama devera escreve na tela se o 
usuário venceu ou perdeu'''

from random import randint

numeroAleatorio = randint(0, 6)
print('Tente advinhar meu numero, está de 0 a 5')
palpite = int(input('Qual o seu palpite? '))

if palpite == numeroAleatorio:
    print('PARABENS!!! VC ACERTOU')
else:
    print('que pena vc errou!')
    print(f'o numero que eu havia escolhido foi {numeroAleatorio}')
    print('tente novamente mais tarde')