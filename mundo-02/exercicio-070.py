'''Crie um programa que leia o nome e o preço de vários produtos. O programa 
deverá perguntar se o usuário vai continuar. No Final mostre:
- Qual o total Gasto na compra;
- Quantos produtos gastam mais de R$1000.00;
- Qual é o nome do produto mais barato.'''

valorTotalGasto = float(0)
maisDeMilReais = float(0)
valorProdutoMaisBarato = float(0)



while True:
    nomeProduto = str(input('Insira o Nome do produto: '))
    valorProduto = float(input('Insira o valor do produto: R$ '))
    
    if valorTotalGasto == 0:
        valorProdutoMaisBarato = valorProduto
        
    valorTotalGasto += float(valorProduto)
    if valorProduto > 1000:
        maisDeMilReais += 1
    
    if valorProduto <= valorProdutoMaisBarato:
        nomeProdutoMaisBarato = str(nomeProduto)
        valorProdutoMaisBarato = valorProduto
    
    continuarCompra = str(input('Deseja continuar Comprando [Y/N]: ')).lower()
    while continuarCompra not in 'yn':
        continuarCompra = str(input('Deseja continuar Comprando [Y/N]: ')).lower()
    if continuarCompra == 'n':
        break  
    
    print('========'* 8)
       
print('//--'* 20)   
print(f'O total gasto na compra foi R$ {valorTotalGasto}')
print(f'{maisDeMilReais} itens custam mais de mil Reais')
print(f'o produto mais barato foi: {nomeProdutoMaisBarato} custando R$ {valorProdutoMaisBarato}')
print('//--' * 20)   