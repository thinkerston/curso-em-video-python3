'''Crie uma função chamada leia dinheiro() que seja capaz de funcionar  como 
função input(), mas com uma validação de dados para aceitar apenas valores 
que sejam monetarios'''
from modulosepacotes.exercicios.exercicio112 import dado
from modulosepacotes.exercicios.exercicio112 import moeda

valor = dado.leiaDinheiro('Insira o valor: ')
porcentagem = dado.leiaProcentagem('Insira uma porcentagem: ')

info = moeda.dados(valor, porcentagem)

moeda.formatado(info)