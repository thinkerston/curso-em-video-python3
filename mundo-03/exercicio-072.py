'''crie um programa que tenha um tupla totalmente preenchida por uma contagem
por extenso de zero até vinte, seu programa deverá ler um numero do teclado 
entre 0 e 20 e mostra-lo por extenso.'''

numerosPorExtenso = ('um', 'dois', 'tres', 'quatro', 'cinco',
                          'seis', 'sete', 'oito', 'nove', 'dez',
                          'onze', 'doze', 'treze', 'catorze', 'quinze',
                          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    numeroConsulta = int(input('de 0 a 20: qual numero deseja consultar? '))
    
    while (numeroConsulta < 0) or (numeroConsulta > 20):   
        print(f'A consulta {numeroConsulta} é invalida')
        numeroConsulta = int(input('insira um numero de 0 a 20: ')) 
        pass
    print(f'Você digitou o numero {numerosPorExtenso[numeroConsulta - 1]}')
    
    sair = str(input('deseja sair? [Y/N]: ')).lower()
    if (sair == 'y'):
        break

print('Obrigado por me usar!')