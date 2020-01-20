'''Faça um mini-sistema que ultiliza interactive Help do python. o usuario vai digitaro comando e o manual
vai aperecer. quando o usuário digitar a palavra "FIM", o programa se encerrará'''

def ajudame():
    funcao = str(input('Insira o nome da funcão: FIM PARA SAIR :')).lower()
    while True:
        if funcao == 'fim':
            return('SAI')
        print(help(funcao))
        funcao = str(input('Insira o nome da funcão: FIM PARA SAIR: ')).upper()
ajudame()