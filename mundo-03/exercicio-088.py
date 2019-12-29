'''Faça um programa que ajude um jogador da megasena a criar palpites. o Programa 
vai perguntar quantos jogo serão gerados e vai sortear 6 numeros entre 1 e 60
para cada jogocadastrado tudo em uma lista composta:'''

from random import randint
from time import sleep

numeroPalpites = int(input('Quantos Palpites deseja gerar: '))
numerosGerados = int(0)
lista = []
listaDePalpites = []
for i in range(0, numeroPalpites):
    
    while numerosGerados < 6:
        palpite = randint(1, 60)
        if palpite not in lista:
            lista.append(palpite)
            numerosGerados += 1

    listaDePalpites.append(lista[:])
    lista.clear()
    numerosGerados = 0            
for linha in listaDePalpites:
    linha.sort()
    print(linha)
    sleep(0.5)