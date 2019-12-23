'''Crie um programa para identificar se a frase digitada é palindroma'''

fraseOriginal = str(input('Insira uma frease: '))
fraseDeVerificacao = str(fraseOriginal.lower().replace(' ', ''))

if fraseDeVerificacao == fraseDeVerificacao[::-1]:
    print('A sua frase:')
    print(fraseOriginal)
    print('É PALIMDROMA')
else:
    print ('A frase não é palimdroma')