'''Faça um algorito que leia o preço de um produto e mostre o seu novo preço com 5% de desconto'''

print('calcule 5 porcento de desconto')
valorAtual = float(input('Insira o valor do produto: '))
ValorDescontado = float(valorAtual - (valorAtual * 0.05))
print(f'O novo valor fica R$:{ValorDescontado}')