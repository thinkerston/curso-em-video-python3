'''Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla
depois disso, mostre a listagem de números gerados e também indique o menor e
o maior valor que estão na tupla'''
from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
            randint(0, 10), randint(0, 10))
print(numeros)
print(f'O menor numero é {min(numeros)}')
print(f'O menor numero é {max(numeros)}')
