'''Faca um programa que leia o peso de cinco pessoas. 
no final, mostre qual foi o maior e o menor peso'''

maiorPeso = float(0)
menorPeso = float(0)

for i in range(0, 5):
    peso = float(input('qual o seu peso: '))
    if peso > maiorPeso:
        maiorPeso = peso
        pass
    elif (menorPeso != peso) and (peso < menorPeso):
        menorPeso = peso
        pass

print('-'*7)
print(f'O menor peso foi de {menorPeso}')
print(f'O maior peso foi de {maiorPeso}')