'''Faça um programa que leia 3 numeros e mostre qual é maior e o menor'''

primeiroNumero = float(input('insira o primeiro numero: '))
segundoNumero = float(input('insira o segundo numero: '))
terceiroNumero = float(input('insira o terceiro numero: '))

if (primeiroNumero > segundoNumero) and (primeiroNumero > terceiroNumero):
    print(f'O maior numero é {primeiroNumero}')
elif (segundoNumero > terceiroNumero) and (segundoNumero > terceiroNumero):
    print(f'O maior numero é {segundoNumero}')
else:
    print(f'O maior numero é {terceiroNumero}')
    
if (primeiroNumero < segundoNumero) and (primeiroNumero < terceiroNumero):
    print(f'O menor numero é {primeiroNumero}')
elif (segundoNumero < terceiroNumero) and (segundoNumero < terceiroNumero):
    print(f'O menor numero é {segundoNumero}')
else:
    print(f'O menor numero é {terceiroNumero}')