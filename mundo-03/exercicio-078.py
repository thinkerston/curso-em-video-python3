'''fça um programa que leia 5 valores e guarde numa lista. No final, mostre qual
foi o maior e o menor valor digitado e suas respectivas posições na lista'''

lista = list()

for i in range(0, 5):
    valor = int(input('Digite um numero inteiro: '))
    lista.append(valor)
    pass

print(f'Você digitou os valores {lista}')
print(f'O maior valor é: {max(lista)}, guardado na posição: {lista.index(min(lista))}')
print(f'O maior valor é: {min(lista)}, guardado na posição: {lista.index(max(lista))}')