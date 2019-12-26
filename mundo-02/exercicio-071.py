'''Crie um programa que simule o funcionamento de um caixa eletronico. no inicio,
pergunte ao usuário qual será o valor sacado (numero inteiro) e o programa vai informar
quantas cedulas de cada valor serão entregues
obs.: considere que o caixa possui cédulas  de R$50, R$20, R$10 e R$1.'''



while True:
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
    
    print(f'Total de {notasCinquenta} Notas de R$ 50')
    print(f'Total de {notasVinte} Notas de R$ 20')
    print(f'Total de {notasDez} Notas de R$ 10')
    print(f'Total de {notasUm} Notas de R$ 1')


    novaOperacao = str(input('Deseja fazer uma nova operacao? [Y/N] ')).lower()
    while novaOperacao not in 'yn':
        novaOperacao = str(input('Deseja fazer uma nova operacao? [Y/N] ')).lower()
    
    if novaOperacao == 'n':
        print('Hasta la vista baby')
        break
    print('========' * 10)