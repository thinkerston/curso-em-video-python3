'''Faça um programa que tenha uma função chamada maior, que receba varios
parâmetros com  com valores inteiros. Seu programa tem que analisar todos
os valores e dizer qual deles é o maior'''
from time import sleep
def Maior (*valores):
    
    if valores == ():
        print('Valores inexistentes')
        return(None)
    
    else:
        print('~~~~~~' * len(valores))
        print('Analisando os valores... ')
        for i in valores:
            print(i, flush=True, end=' ')
            sleep(0.3)
        print(f'Foram informados {len(valores)} ao todo')
        print(f'O maior valor informado foi {max(valores)}')
        print('~~~~~~' * len(valores))
    
Maior(1, 2, 6, 7, 5, 7, 147)
Maior()