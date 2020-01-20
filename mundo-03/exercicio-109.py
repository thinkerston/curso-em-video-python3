'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem
um parametro a mais, informando se o valor retornado por elas vai ser ou não
formatado pela função moeda desenvolvida no desafio 108.'''
from modulosepacotes.exercicios.exercicio109 import moeda


valor = float(input('insira um valor: '))
porcentagem = float(input('Insira uma porcentagem: '))

formatar = str(input('Deseja formatar ? [Y/N] ')).lower()

if formatar == 'y':
    moeda.formatado(valor, porcentagem)
    pass
else:
    moeda.naoFormatado(valor, porcentagem)