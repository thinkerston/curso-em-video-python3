'''Crie um programa onde o usuário possa digitar 7 valores númericos e cadastre-os em uma unica lista que mantenha separados os valores pares e impares.
no final mostre os valores pares e impares em ordem crescente''' 

lista = [[], []]


for i in range(0, 7):
    numero = int(input('insira um numero: '))
    
    
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

lista[0].sort()
lista[1].sort()
     

print(f'Os pares digitados foram {lista[0]}')
print(f'Os impares digitados foram {lista[1]}')



