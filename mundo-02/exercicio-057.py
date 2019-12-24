'''faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores 'M' ou 'F'. caso esteja errado, peça novamente até ter um 
valor correto'''

sexo = str(input('insira seu sexo [M] ou [F]: ')).lower().strip()

while sexo not in 'fm':
    sexo = str(input('insira seu sexo [M] ou [F]: ')).lower().strip()

if sexo == 'm':
    print('obrigado senhor')
else:
    print('obrigado senhora')