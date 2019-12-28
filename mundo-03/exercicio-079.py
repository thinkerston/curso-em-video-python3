'''Crie um programa onde o usuário possa digitar vários valores númericos e 
cadastre-os em uma lista. caso o numero já exista lá dentro, ele não será 
adicionado. no final, serão exibidos todos os valores únicos digitados, em 
ordem crescente'''

lista = list()

while True:
    adicionarNaLista = int(input('Qual numero deseja inserir na lista: '))
    
    
    if adicionarNaLista not in lista:
        print(f'{adicionarNaLista} foi adicionado')
        lista.append(adicionarNaLista)
        pass
    else:
        print('valor Duplicado. não será adicionado')

    sair = str(input('Deseja sair? Y/N: ')).lower()    
    if sair == 'y':
        break
    
lista.sort()
print(f'Os valores unicos digitados em ordem crescente foram {lista}')
    