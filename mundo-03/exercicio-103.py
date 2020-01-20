'''Faça um programa que tenha uma função chamada ficha, que receba dois parametros
opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá
ser capaz de mostrar a  ficha do jogador, mesmo que algum dado não tenha sido 
informado corretamente'''

def ficha(nome=str('<Desconhecido>'), gols=str(0)):
    informacao = str((f'o Jogador {nome} fez {gols} gol(s), no campeonato!'))
    return(informacao)
    
nomeJogador = str(input('Insira o nome do jogador: '))
numeroGols = str(input('Insira o numero de Gols: '))



if nomeJogador == '' and numeroGols == '':
    print(ficha())
    pass
elif nomeJogador == '':
    print(ficha(gols=numeroGols))
    pass
elif numeroGols == '':
    print(ficha(nome=nomeJogador))
    pass
else:
    print(ficha(nomeJogador, numeroGols))
    pass