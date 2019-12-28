''' Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os valores pares e 
 os valores ímpares digitados respectivamentes. ao final mostreo conteúdo das
 três listas geradas'''
''' '''

 
lista = list()
listaPar = list()
listaImpar = list()

while True:
    numero = int(input('insira um numero: '))
    lista.append(numero)
    
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
    
    sair = str(input('deseja sair: Y/N: ')).lower()
    while sair not in 'yn':
        sair = str(input('deseja sair: Y/N: ')).lower()

    if sair == 'y':
        break
    

            
print(f'todos os numeros digitados foram {lista}')
print(f'Os pares digitados foram {listaPar}')
print(f'Os impares digitados foram {listaImpar}')



