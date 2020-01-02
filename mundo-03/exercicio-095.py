'''Aprimore o desafio 093 para que ele funcione com varios jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador'''


totalGols = int(0)
dadosJogador = dict()
listaTodosJogadores = []
listaGols = []

while True:
    nomeJogador = str(input('Insira o nome do Jogador: '))
    numeroPartidas = int(input('Insira o numero de partidas que ele jogou: '))
    for partida in range(0, numeroPartidas):
        gols = int(input(f'Insira o total de gols na partida {partida + 1} : '))
        
        listaGols.append(gols)
        

        
        pass
    dadosJogador['nome'] = nomeJogador
    dadosJogador['n partidas'] = numeroPartidas
    dadosJogador[f'gols'] = listaGols[:]
    dadosJogador['total de gols'] = sum(listaGols)
    listaGols.clear()
    listaTodosJogadores.append(dadosJogador.copy())
    print(listaTodosJogadores)
    sair = str(input('Deseja sair? Y/N: ')).lower()
    while sair not in 'yn':
        sair = str(input('Deseja sair? Y/N: ')).lower()
    if sair == 'y':
        break
contador = int(0)

print('id  nome   gols    total')
for jogador in listaTodosJogadores:
    
    print(contador, end= '  ')
    print(jogador['nome'], end='  ')
    print(jogador['gols'], end='  ')
    print(jogador['total de gols'])
    contador += 1
    pass
print('=======' * 8)

while True:
    nJogadorIndice = int(input('Insira o numero do jogador que deseja ver: '))
    if nJogadorIndice < 0 or nJogadorIndice > int(len(listaTodosJogadores) - 1):
        print('O jogador não está no indice')
    else:
        consultaJogador = listaTodosJogadores[nJogadorIndice ]

        print('=======' * 8)
        for chave, valor in consultaJogador.items(): 
            print(chave, valor)
            
        finalizar = str(input('Deseja sair? Y/N: ')).lower()
        while finalizar not in 'yn':
            if finalizar not in 'yn':
                finalizar = str(input('Deseja sair? Y/N: ')).lower()
                pass
        if finalizar == 'y':
            break

            
            

