'''Crie um programa que simule o funcionamento de um caixa eletronico. no inicio,
pergunte ao usuário qual será o valor sacado (numero inteiro) e o programa vai informar
quantas cedulas de cada valor serão entregues
obs.: considere que o caixa possui cédulas  de R$50, R$20, R$10 e R$1.'''

print('O caixa possui cedulas de R$50, R$20, R$10 e R$1')
valorSacado = int(input('Insira o valor a ser sacado: '))
valorRestante = int(0)
notasCinquenta = int(0)
notasVinte = int(0)
notasDez = int(0)
notasUm = int(0)

notasCinquenta = valorSacado // 50
valorRestante = valorSacado % 50

notasVinte = valorRestante // 20
valorRestante = valorRestante % 20

notasDez = valorRestante // 10
valorRestante = valorRestante % 10

notasUm = valorRestante // 1
valorRestante = valorRestante % 1

print(notasCinquenta)
print(notasVinte)
print(notasDez)
print(notasUm)

'''Optei fazer sem While por ser mais facil'''