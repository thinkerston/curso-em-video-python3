'''faça um programa que tenha a função contador que receba três paremetros:
inicio, fim e passo e realiza a contagem:'''
from time import sleep


def contadoresInicio():
    for j in range (1, 11, 1):
        print(j, flush=True, end=' ')
        sleep(0.4)
    
    for k in range(10, 0, -2):
        print(k, flush=True, end=' ')
        sleep(0.5)
        pass
    pass
        

def Contador(inicio, fim, passo):
    print(f'Contagem de 1 até 10')
    for j in range (1, 11, 1):
        print(j, flush=True, end=' ')
        sleep(0.4)
        pass
    print('\n')
    
    print(f'Contagem de 10 até 0')
    for k in range(10, -2, -2):
        print(k, flush=True, end=' ')
        sleep(0.5)
        pass
    print('\n')
        
    if (passo == 0):
        passo = 1
        pass
    
    print(f'Contagem personalizada de {inicio} até {fim} pulando de {passo}')
    
    if fim > inicio:
        if passo > 0:
            for i in range(inicio, fim + 1, passo):
                print (i, flush=True, end=' ')
                sleep(.3)
                pass
            pass
        else:
            for i in range(inicio, fim + 1, -passo):
                print (i, flush=True, end=' ')
                sleep(.3)
                pass
            pass
        
        
    elif inicio > fim:
        if passo > 0:
            for i in range (inicio, fim - 1 , -passo):
                print (i, flush=True, end=' ')
                sleep(.3)
                pass
            pass
        else:
                for i in range (inicio, fim - 1, passo):
                    print (i, flush=True, end=' ')
                    sleep(.3)
                pass

    print('\n')
    pass


inicio = int(input('Insira o inicio: '))
fim = int(input('Insira o fim: '))
passo = int(input('Insira o Passo: '))


Contador(inicio, fim, passo)