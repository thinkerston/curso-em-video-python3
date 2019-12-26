'''Crie uma tupla com várias palavras (sem acento). Você deve mostrar, para cada palavra,
quais são suas vogais.'''

tuplaPalavras = ('Adeus','Amor','Chuva','Cuidar','Enfemeiro','Enternecer','Adoravel','Caminhos','Coragem','Cumplicidade','Equilibrio','Esperança')
for palavra in tuplaPalavras:
    print(f'Na palavra {palavra},as vogais são: ', end='')
    for letras in palavra:
        if letras in 'aeiouAEIOU':
            print(letras, ' ', end='')
    print('\n')