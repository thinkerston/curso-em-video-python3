'''Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

- a vista dinheiro/cheque: 10% de desconto;
- a vista no cartão: 5%;
- em até 2x vezes no cartão: Preço normal;
-3x ou mais no cartão: 20% de juros.
'''

valorProduto = float(input('qual o valor do Produto? '))
print('como deseja pagar')
print('1 - AVISTA no dinheiro/cheque: -10%')
print('2 - AVISTA no Cartão: -5%')
print('3 - em até 2x: preço normal')
print('4 - 3x ou mais no cartão: +20% ')
formaPagamento = int(input('Qual das formas acima? '))

if formaPagamento == 1:
    novoValorProduto = float( valorProduto - (valorProduto * 0.10))
    print(f'Você pagara R$ {novoValorProduto}')
    pass
elif formaPagamento == 2:
    novoValorProduto = float( valorProduto - (valorProduto * 0.05))
    print(f'Você pagara R$ {novoValorProduto}')
    pass
elif formaPagamento == 3:
    print(f'Você pagara R$ {valorProduto}')
    pass
elif formaPagamento == 4:
    novoValorProduto = float( valorProduto + (valorProduto * 0.2))
    print(f'Você pagara R$ {novoValorProduto}')
    pass
else:
    print('a forma de pagamento selecionada não corresponde a nenhuma')