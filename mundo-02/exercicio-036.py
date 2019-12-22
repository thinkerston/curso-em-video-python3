'''Escreva um programa para aprovar um emprestimo bancário ára compra de
uma casa. O programa vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo
que ela não pode exceder 30% do salário ou então o emprestimo será negado'''

valorImovel = float(input('Qual o valor do imóvel? '))
tempoParaPagar = int(input('Em quantos anos deseja pagar? '))
salario = float(input('qual o seu salário? '))

valorPrestacao = float((valorImovel) / (tempoParaPagar * 12))

if (valorPrestacao > (salario * 0.3)):
    print('infelizmente não podemos fornecer o imprestimo para você')
else:
    print('Parabéns o seu impréstimo foi aporovado')
    
print(f'O valor da prestação é R${valorPrestacao:0.2f}')