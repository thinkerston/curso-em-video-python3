'''Faça um programa que mostre a tabuada de vários numeros, um de cada vez para cada valor
digitado pelo usuário. O programa será interrompido quando o numero solicitado for negativo'''

while True:
    numero = int(input('insira o numero para ver a tabuada e numero negativo para sair: '))
    if numero < 0:
        print('Obrigador por me usar')
        break
    else:
        for i in range(1, 11):
            print(f'{numero} x {i} = {numero * i} ')
        pass