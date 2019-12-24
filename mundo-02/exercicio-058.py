# Simple Man - Lynyrd Skynyrd
'''Melhore o exercicio 028, onde o computador vai 'pensar' em um numero 
entre 0 e 10. só que agora o jogador vai tentar adivinhar até acertar, 
mostrando quantos palpites foram necessários para vencer'''

from random import randint

numeroAleatorio = randint(0, 11)
print('Tente advinhar meu numero, está de 0 a 10')
palpite = int(input('Qual o seu palpite? '))
numeroDePalpites = int(1)

while palpite != numeroAleatorio:
    numeroDePalpites += 1
    palpite = int(input('Qual o seu palpite? '))
    print('Affs!! vc errou')
    
if palpite == numeroAleatorio:
    print('PARABENS!!! VC ACERTOU')
    print(f'você precisou de {numeroDePalpites} vezes para acertar')
