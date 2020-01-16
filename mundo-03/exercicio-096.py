'''Faça um programa que tenha uma função chamada Area(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno'''

def Area(largura, comprimento):
    print(f'A area do terreno é {(largura * comprimento)}m² ')

largura = float(input('Insira a Largura do terreno: '))
comprimento = float(input('Insira o Comprimento do terreno: '))

Area(largura, comprimento)
