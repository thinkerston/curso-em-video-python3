'''Refaça o exercicio 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while'''

primeiroTermo = int(input('Insira o primeiro termo: '))
razao = int(input('insira a razão: '))
progressaoArentimetica = int(0)
contador = int(1)

while contador < 11:
    progressaoArentimetica = int(primeiroTermo + (contador - 1) * razao)
    print(progressaoArentimetica)
    contador += 1