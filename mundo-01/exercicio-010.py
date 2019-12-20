'''crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar'''


dolar = float(input('quanto está valendo o dolar? '))
dinheiroNaCarteira = float(input('quanto pretende comprar? '))
realParaDolar = float(dinheiroNaCarteira/dolar)
print(f'Com o dolar a {dolar} você podera comprar {realParaDolar:0.2f}')