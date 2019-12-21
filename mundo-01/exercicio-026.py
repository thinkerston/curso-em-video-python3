'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Insira uma frase: ')).lower()
encontrandoLetra = frase.count('a')
primeiraLetra = frase.find('a')
ultimaLetra = frase.rfind('a')

print(f'sua frase contém {encontrandoLetra} Letras "A"')
print(f'A primeira aparição da letra "A" aparece em {primeiraLetra + 1}')
print(f'A utlima aparição da letra "A" aparece em {ultimaLetra + 1}')