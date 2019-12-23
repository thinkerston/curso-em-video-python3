'''Desenvolva um programa qie leia o primeiro termo e a razão de uma PA. 
no final, mostre os 10 primeiros termos dessa progressão'''

primeiroTermo = int(input('Insira o primeiro termo: '))
razao = int(input('insira a razão: '))
progressaoArentimetica = int(0)


for i in range(1, 11):
    progressaoArentimetica = int(primeiroTermo + (i - 1) * razao)
    print(progressaoArentimetica)
