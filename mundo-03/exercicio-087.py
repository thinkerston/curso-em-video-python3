'''crie um programa que crie uma matriz de dimensão 3x3 e preencha os valores lidos
pelo teclado. no final mostre a matriz na tela, com a formatação correta e mostre:
-A soma de todos os valores pares digitados;
-A soma de todos os valores pares da segunda coluna;
-O maior valor da segunda linha
'''

matriz = [[], [], []]
valorPar = []
maiorValor = int(0)
somaValoresPares = int(0)
somaValoresTerceiraColuna = int(0)
for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f'insira um valor inteiro na posição {i, j}: da matriz: '))
        if (valor % 2 == 0):
            somaValoresPares += valor
            pass
        if j == 2:
            somaValoresTerceiraColuna += valor
        if (i == 1) and (valor > maiorValor):
            maiorValor = valor
        matriz[i].append(valor)

print('======='*8)
for l in range(0, 3):
    print(matriz[l])

print(f'A soma de todos valores pares são {somaValoresPares}')
print(f'A soma dos valores da terceira coluna é {somaValoresTerceiraColuna}')
print(f'O maior valor da Segunda linha é {maiorValor}')