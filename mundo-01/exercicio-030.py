'''Crie um program aque leia se o numero inteiro e mostre se ele é impar ou par'''

numero = int(input('insira seu numero: '))

if (numero % 2) == 0:
    print(f'O numero {numero} é par')
else:
    print(f'O numero {numero} é impar')