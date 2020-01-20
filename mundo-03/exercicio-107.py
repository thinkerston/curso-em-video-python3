'''Crie um modulo chamado moeda.py que tenhas as funções incorporadas aumentar(),
diminuir, dobro() e metade().

faça também um programa que importe esse modulo e use algumas dessas funções'''

from modulosepacotes.exercicios.exercicio107 import moeda

valor = float(input('insira um valor: '))
porcentagem = float(input('Insira uma porcentagem: '))

print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'A dobro de {valor} é {moeda.dobro(valor)}')
print(f'aumentando de {valor} em {porcentagem} é {moeda.aumentar(valor, porcentagem)}')
print(f'diminuindo de {valor} em {porcentagem} é {moeda.diminuir(valor, porcentagem)}')
