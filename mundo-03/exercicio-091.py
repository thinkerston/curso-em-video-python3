'''Crie um programa onde 4 jogadores joguem um dado e tenha resultados 
aleatórios. Guarde esses resultados em um dicionário. No final coloque esse
dicionário em ordem. sabendo que o vencedor tirou o mair número no dado'''
from random import randint
from time import sleep
jogadoresEJogos = dict()

for i in range(0, 4):
    sorteio = randint(1, 6)
    print(f'o {i + 1}° Jogador  tirou no dado o numero {sorteio}')
    jogadoresEJogos[f'{i + 1}° Jogador'] = sorteio
    sleep(0.2)

print('RANKING')
for item in sorted(jogadoresEJogos, key=jogadoresEJogos.get, reverse=True):
    print(item, end=' ')
    print(jogadoresEJogos[item])
    sleep(0.21)