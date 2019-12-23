'''faça um programa  que mostre na tela uma contagem regressiva para estouro de fogos de artificio,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
from time import sleep

for i in range(10, -1, -1):
    print(f'faltam {i} segundos')
    sleep(1)
print('AE!!! JÁ É ANO NOVO')