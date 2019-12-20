'''Escreva um programa que pergunte a quantidade de km percorridos 
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
calcule o preço a pagar, sabedo que o carro custa R$60 por dia e
R$0.15 por km rodado'''

diasAlugados = int(input('quntos dias ele ficou alugado: '))
kmRodados = float(input('quantos Km o carro rodou? '))


valorTotal = float((diasAlugados * 60) + (kmRodados * 0.15))
print(f'O valor a ser pago é R${valorTotal}')