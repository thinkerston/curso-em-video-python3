'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente 
de 0, o dicionário também receberpa o ano de contratação e o salário. Calcule
e acrescente, além da idad, com quantos anos a pessoa vai se aposentar'''
from datetime import date

anoAtual = date.today().year

nome = str(input('Insira seu nome: '))
nascimento = int(input('Insira seu ano de Nascimento: '))
numeroCTPS = int(input('Insira seu CTPS [0 Não possui]: '))
idade = int(anoAtual - nascimento)
dados = dict()
dados['Nome'] = nome
dados['Idade'] = idade
dados['CTPS'] = numeroCTPS

if numeroCTPS != 0:
    anoContratacao = int(input('Insira seu ano de Contratação: '))
    salario = float(input('Insira Seu salário: '))
    dados['Ano'] = anoContratacao
    dados['Salário'] = salario
    dados['Idade Aposentadoria'] = int(idade + abs((anoAtual - anoContratacao) - 35))
    print(anoAtual - anoContratacao)
    pass


for chave, valor in dados.items():
    print(f'O {chave}, tem valor {valor}')