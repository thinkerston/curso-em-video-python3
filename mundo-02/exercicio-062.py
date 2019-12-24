#wanted dead or alive - bon jovi

'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar 
mais alguns termos. o programa encerra quando ele disse que mostrar 0 termos'''

primeiroTermo = int(input('Insira o primeiro termo: '))
razao = int(input('insira a razão: '))
progressaoArentimetica = int(0)
contador = int(1)
limite = int(11)

while contador < limite:
    progressaoArentimetica = int(primeiroTermo + (contador - 1) * razao)
    print(progressaoArentimetica)
    contador += 1
    if contador == limite:
        verMais = str(input('Deseja mais quantos termos?, insira 0 para sair: '))
        limite += int(verMais)
        if verMais == 0:
            contador = limite
            pass

print('obrigado por usar nosso programa')