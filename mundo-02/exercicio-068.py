'''crie um programa que jogue par ou um impar com o computador. O jogo só será interrompido
quando o jogador perderm mostrando o total de vitórias consecutivas que ele conquistou no final do jogo'''
from random import randint

contaVitorias = int(0)

while True:
    parOuImpar = str(input('Escolha entre [P]par ou [I]impar: ')).lower()
    if parOuImpar not in 'pi':
        print('A sua escolha não corresponde a um valor valido')
    else:
        valorEscolhidoUsuario = int(input('Escolha um valor para a disputa: '))
        valorEscolhidoComputador = int(randint(0, 10))
        somaEscolhas = int(valorEscolhidoUsuario + valorEscolhidoComputador)
        
        print(f'você escolheu {valorEscolhidoUsuario}')
        print(f'o computador escolheu {valorEscolhidoComputador}')
        print(f'A soma é {somaEscolhas}')
        if parOuImpar == 'p':
            if (somaEscolhas % 2 == 0):
                contaVitorias += int(1)
                print('Parabéns Você venceu')
                pass
            else:
                print('Você Perdeu')
                break
                
        else:
            if (somaEscolhas % 2 == 1):
                contaVitorias += int(1)
                print('Parabéns Você venceu')
                pass
            else:
                print('Você Perdeu')
                break
                
            pass
        pass
    print('******' * 10)
    


print(f'voce teve {contaVitorias} vitórias antes de perder')