'''Crie um programa que faça o computador jogar JOKENPÔ com vc'''
from random import randint

print('Escolha um numero para jogar')
print('1 - Pedra')
print('2 - papel')
print('3 - tesoura')
numeroUsuario = int(input('ESCOLHA: '))
numeroComputador = randint(1, 3)
jokenpo = ['pedra','papel', 'tesoura']
print(numeroUsuario)
print(numeroComputador)

print(f'{jokenpo[numeroUsuario - 1]} x {jokenpo[numeroComputador - 1]}')


if numeroUsuario == numeroComputador:
    print('HOUVE UM EMPATE')
    pass
elif numeroUsuario == 1:
    if numeroComputador == 2:
        print('Você PERDEU')
        pass
    else:
        print('PARABENS VC GANHOU')
        pass
    pass
elif numeroUsuario == 2:
    if numeroComputador == 3:
        print('Você PERDEU')
        pass
    else:
        print('PARABENS VC GANHOU')
        pass
    pass
elif numeroUsuario == 3:
    if numeroComputador == 1:
        print('Você PERDEU')
        pass
    else:
        print('PARABENS VC GANHOU')
        pass
    pass
else:
    print('JOGADA INVALIDA')
    pass