'''FAça um programa que calcule a soma entre todos os numeros ímpares 
que são multiplos de três e que se encontram no intervalo de 1 a 500'''

print('Mostrando todos os numeros impares, multiplos de 3 de 1 até 500')

soma = int(0)
for i in range(0, 501):
    if (i % 2 != 0) and (i % 3 == 0):
        soma += i

print(soma)