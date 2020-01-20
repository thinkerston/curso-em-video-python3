'''Adapte o código desafio 107, criando uma função adicional chamada moeda108() que
consiga mostrar os valores como um valor monetário formatado'''

from modulosepacotes.exercicios.exercicio108 import moeda

valor = float(input('insira um valor: '))
porcentagem = float(input('Insira uma porcentagem: '))

print(f'A metade é {moeda.metade(valor)}')
print(f'A dobro  é {moeda.dobro(valor)}')
print(f'aumentando  em {porcentagem:.0f}% é {moeda.aumentar(valor, porcentagem)}')
print(f'diminuindo  em {porcentagem:.0f}% é {moeda.diminuir(valor, porcentagem)}')
