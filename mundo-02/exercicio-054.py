'''Crie um programa que leia o ano de nascimento de sete pessoas.
no final, mostre quantas pessoas ainda mão atingiram a maioridade e 
quantas já são maiores - considere maioridade a partir de 21 anos'''
from datetime import date

anoAtual = date.today().year
idade = int(0)
maioridade = int(0)
menoridade = int(0)

for i in range(0, 7):
    
    anoNascimento = int(input('Insira o seu ano de nascimento: '))
    idade = int(anoAtual - anoNascimento)
    if idade >= 21:
        maioridade += 1
    else:
        menoridade +=1

print('Nessa dados nós temos:')
print(f'{maioridade} : Maiores de 21 anos')
print(f'{menoridade} : Menores de 21 anos')
