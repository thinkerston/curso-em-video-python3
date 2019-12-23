'''refaça o desafio 009, mostrando a tabuada de um numero 
que o usuário escolher, só que agora ultilizando o laço for'''

numeroTabuada = int(input('insira o numero que de seja ver a tabuada: '))

for i in range(1, 11):
    print(f'{numeroTabuada} x {i} == {numeroTabuada * i}')