from math import sqrt, pow

'''crie um programa que leia o comprimento do cateto oposto,
e do cateto adjacente de um triangulo retangulo, calcule
e mostre o comprimento da hipotenusa'''

catetoOposto = float(input('Insira o cateto oposto: '))
catetoAdjacente = float(input('Insira agora o cateto Adjacente: '))
hipotenusa = float(sqrt(pow(catetoOposto, 2)+(pow(catetoAdjacente, 2))))

print(f'A hipotenusa é {hipotenusa}')