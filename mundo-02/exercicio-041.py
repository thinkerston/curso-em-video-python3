'''A confederação nacional de natação precisa de um programa que leia 
o ano de nascimento de um atleta e mostre sua categoria , de acordo com a idade:

- Até 9 anos: mirim
- Até 14 anos: infantil
- Até 19 anos: junior
- Até 20 anos: senior
- acima: master'''

from datetime import date

dataNascimento = int(input('Insira o Ano que você nasceu: '))
dataAtual = date.today()
anoAtual = int(dataAtual.strftime('%Y'))
print(' ')

if (anoAtual - dataNascimento) <= 14:
    print('Você é um atleta MIRIM')
    pass
elif(anoAtual - dataNascimento) <= 14:
    print('Você é um atleta INFANTIL')
    pass
elif (anoAtual - dataNascimento) <= 19:
    print('Você é um atleta JUNIOR')
    pass
elif (anoAtual - dataNascimento) <= 20:
    print('Você é um atleta SENIOR')
    pass
else:
    print('Você é um atleta MASTER')
    pass