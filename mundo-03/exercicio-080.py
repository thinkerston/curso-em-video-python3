'''Crie um programa onde o usuário possa digitar cinco valores numéricos e 
cadastre-os en uma lista, ja na posição correta de inserção (sem usar o sort())
no final, mostre a lista a lista ordenada na tela'''

lista = []

for i in range(1, 6):
    adicionar = int(input(f'[{i}/5] Digite um valor: '))

    maior = 0

    if len(lista) > 0:
        for número in lista:
            if maior < número < adicionar:
                maior = número

        if maior != 0:
            lista.insert(lista.index(maior) + 1, adicionar)
        else:
            lista.insert(0, adicionar)
    else:
        lista.append(adicionar)

print('-+' * 20)
print(f'Você digitou: {str(lista)[1:-1]}.')
print('-+' * 20)


