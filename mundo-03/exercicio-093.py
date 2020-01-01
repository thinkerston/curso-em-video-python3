'''Crie um programa que gerencie o Aproveitamento de um Jogador de futebol.
O programa vai ler o nom do jogador e quantas partidas ele jogou. Depois vai ler
a quantidade de gols que fez em cada partida. no final tudo isso será guardado em 
um dicionário, incluindo o total de gols feitos durante o campeonato'''

nomeJogador = str(input('Insira o nome do Jogador: '))
numeroPartidas = int(input('Insira o numero de partidas que ele jogou: '))
totalGols = int(0)
dadosJogador = dict()
dadosJogador['Nome'] = nomeJogador

for partida in range(0, numeroPartidas):
    gols = int(input(f'Insira o total de gols na partida {partida + 1} : '))
    totalGols += gols
    dadosJogador[f'gols da  {partida + 1}° Partida'] = gols
    pass

dadosJogador['Total de gols'] = int(totalGols)  
print('======'*6, end='\n')
print(f'O jogador {nomeJogador} jogou {numeroPartidas} partidas')
print('======'*6, end='\n')
for chave, valor in dadosJogador.items():
    print(f'O {chave}, tem valor {valor}')