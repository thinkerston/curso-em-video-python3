from random import shuffle

'''Um professor quer sortear a ordem de apresentação de trabalhos
de 4 alunos. Faça um programa que leia o nome deles e mostre a ordem sorteada'''

aluno1 = str(input('Insira o nome do primeiro aluno: '))
aluno2 = str(input('Insira o nome do segundo aluno: '))
aluno3 = str(input('Insira o nome do terceiro aluno: '))
aluno4 = str(input('Insira o nome do quarto aluno: '))
ordem = [aluno1, aluno2, aluno3, aluno4]
shuffle(ordem)

print('a ordem de apresentação é: ')
print(ordem)