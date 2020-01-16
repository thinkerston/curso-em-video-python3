'''Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocar-los
dentro da lista e a segunda função vai mostrar a soma entre todos valores pares
sorteados pela função anterior'''

from random import randint

def Sorteia():
    sorteados = []
    for i in range(0, 5):
        sorteados.append(randint(0, 9999999999))
    print(f'Os numeros sorteados foram {sorteados}')
    return(sorteados)


def SomaPar(lista):
    somaPares = int(0)
    pares = []
    for i in lista:
        if i % 2 == 0:
            somaPares += i
            pares.append(i)
            pass
        pass
    print(f'A soma de {pares} é {somaPares}')
    pass
         

lista = Sorteia()
SomaPar(lista)