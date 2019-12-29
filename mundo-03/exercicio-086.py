'''crie um programa que crie uma matriz de dimensão 3x3 e preencha os valores lidos
pelo teclado. no final mostre a matriz na tela, com a formatação correta'''

matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'insira um valor inteiro na posição {i, j}: da matriz: ')))
print('======='*8)
for l in range(0, 3):
    print(matriz[l])