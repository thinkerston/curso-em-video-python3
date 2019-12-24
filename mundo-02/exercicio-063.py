'''Escreva um programa que leia um numero 'n' inteiro qualuqer e mostre 
na tela os 'n' primeiros elementos de uma sequencia de fibonacci'''

numeroDeTermos = int(input('insira o numero de termos que deseja ver de uma sequência de fibonacci: '))
contador = int(0)
termoAnterior = int(0)
termoAtual = int(1)

while contador < numeroDeTermos:
    print(termoAnterior)
    print(termoAtual)
    termoAnterior += termoAtual
    termoAtual += termoAnterior
    contador += 1
    