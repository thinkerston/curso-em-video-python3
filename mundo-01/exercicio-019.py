from random import choice

'''Um professor quer sortear um dos seus alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o
nome do escolhido na tela'''

aluno1 = str(input('Insira o nome do primeiro aluno: '))
aluno2 = str(input('Insira o nome do segundo aluno: '))
aluno3 = str(input('Insira o nome do segundo aluno: '))
aluno4 = str(input('Insira o nome do segundo aluno: '))

print('O aluno escolhido é ', end='')
print(choice([aluno1, aluno2, aluno3, aluno4]))
