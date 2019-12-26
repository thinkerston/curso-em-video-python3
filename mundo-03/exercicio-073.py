'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato
brasileiro de futebol. na ordem de colocação. Depois mostre?
- Apenas os 5 primeiros colocados;
- os ultimos 4 colocados;
- uma lista de times em ordem alfabetica;
- em que posição esta  o time da Chapecoense.'''

tabelaBrasileirao = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Athletico-PR',
                     'São Paulo', 'Internacional', 'Corinthias', 'Fortaleza',
                     'Goias', 'Bahia', 'Vasco', 'Atletico-MG','Fluminense',
                     'Botafogo','Ceará SC','Cruzeiro','CSA','Chapecoense','Avaí')
while True:
    print('Menu Consulta')
    print('''
        [1] veja os 5 primeiros colocados
        [2] veja os 4 ultimos colocados
        [3] veja uma lista em ordem alfabetica
        [4] veja em que posição está o Chapecoense
        [5] insira a posição para ver o time
        [0] Sair
        ''')
    escolhaUsuario = int(input(': '))
    
    if escolhaUsuario == 0:
        break
    elif escolhaUsuario == 1:
        for posicao in range(1, 6) :
            print(f'{posicao}° {tabelaBrasileirao[posicao -1]}')
            print('====='*5)
        pass
    elif escolhaUsuario == 2:
        for posicao in range(16, 20):
            print(f'{posicao +1 }° {tabelaBrasileirao[posicao]}')
            print('====='*5)
        pass
    elif escolhaUsuario == 3:
        tabelaBrasileiraoPorNome = sorted(tabelaBrasileirao)
        for time in (tabelaBrasileiraoPorNome):
            print (time)
            print('==='*5)
        pass
    elif escolhaUsuario == 4:
        print('Chapecoense está na ', end='')
        print((tabelaBrasileirao.index('Chapecoense')+ 1), end='')
        print('° Posição')
        pass
    
    elif escolhaUsuario == 5:
        posicaoConsulta = int(input('Insira a posição que deseja Consultar: '))
        while (posicaoConsulta < 0) or (posicaoConsulta > 20):   
            print(f'A consulta {posicaoConsulta} é invalida')
            posicaoConsulta = int(input('insira um numero de 0 a 20: ')) 
            pass
        print('====='*15)
        print(f'O time que se enconta na posição {posicaoConsulta}° é o {tabelaBrasileirao[posicaoConsulta - 1]}')
        print('====='*15)
        
        pass
    
    else:
        print('A Escolha é invalida Tente novamente com um numero do menu valido')
        pass