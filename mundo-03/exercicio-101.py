'''Crie um programa que tenha função chamada voto() que vai receber como parâmetro
o ano nascimento de uma pessoa, retornando um valor literal indicando se uma
pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições'''

from datetime import date
anoAtual = date.today().year

def voto(nascimento):
    
    
    idade =   anoAtual - nascimento
    
    if idade < 16:
        return('NEGADO')
    elif (idade >= 16) and (idade < 18) or (idade > 65):
        return('OPCIONAL')
    else:
        return('OBRIGATÓRIO')
    
anoNascimento =  int(input('Em que ano vc nasceu: '))

print(f'Com {anoAtual - anoNascimento} o Voto é {voto(anoNascimento)} ')