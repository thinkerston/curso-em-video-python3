'''Faça um programa que leia o ano de nascimento de um jovem  e informe, 
de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar;
- Se é hora de se alistar;
- se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou passou'''

from datetime import date

dataNascimento = int(input('Insira o Ano que você nasceu: '))
sexo = str(input('Insira o seu Sexo biologico [M]masculino, [F]feminino: ')).lower()
dataAtual = date.today()
anoAtual = int(dataAtual.strftime('%Y'))
print(' ')

if sexo == 'm':
    idade = int(anoAtual - dataNascimento)
    if (anoAtual - dataNascimento)  == 18:
        print('você tem exatamente 18 anos, está na hora de se alistar')
        pass
    elif (anoAtual - dataNascimento) > 18:
        print(f'NOSSA VOCÊ PASSOU {idade - 18} de se alistar')
        print(f'VÁ URGENTEMENTE A JUNTA DE SERVIÇO MILITAR NAIS PROXIMA')
        pass   
    else:
        anosRestantes = int(18 - idade)
        print(f'nossa ainda falta {18 - idade} anos para se alistar')
        print(f'No ano de {anoAtual + anosRestantes} vá a junta de serviço militar')
        pass
else:
    print('Atualmente mulheres não são obrigadas a comparacer a junta de serviço militar')
    print('Todavia sao totalmente livreas para servir a pátria caso queiram')
    pass