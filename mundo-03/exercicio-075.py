'''Desevolva um programa que leia quatro valores pelo teclado e guarde-os em 
uma tupla. no final mostre:
-Quantas vezes o apareceu o valor 9;
-em qual posição foi digitado o primeiro valor 3;
-Quais foram os numeros pares.'''

numeros = (int(input('digite um numero: ')),
           int(input('digite um numero: ')),
           int(input('digite um numero: ')),
           int(input('digite um numero: ')))

print(f'O numero 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 apareceu pela primeira na posiçao {numeros.index(3)} ')
else:
    print('O numero 3 Não apareceu ')
print('Os numeros pares são ', end='')

for numero in numeros:
    if (numero % 2 == 0):
        print(numero, end=' ')

