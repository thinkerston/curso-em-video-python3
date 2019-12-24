'''crie um programa que leia varios numeros inteiros pelo teclado. no final
da execução, mostre a média entre todos os valores e qual foi o maior e o
menor valores lidos. o programa deve perguntar ao usuário se ele quer 
ou não a digitar valores'''

valor = int(input('Insira valor para obter a média: '))
numeroDeTermos = int(0)
somaTotal = int(0)
digitarMais = bool(True)
maiorValor = int(valor)
menorValor = int(valor)

while digitarMais == True:
        
    desejaDigitar = str(input('deseja Digitar mais Y/N? ')).lower()
    if desejaDigitar == 'n':
        digitarMais = bool(False)    
        pass
    else:
        valor = int(input('Então insira um novo Valor: '))
        numeroDeTermos += 1
        somaTotal += int(valor)
               
        if valor > maiorValor:
            maiorValor = valor
            pass
        elif valor < menorValor:
            menorValor = valor
            pass
        pass

media = float(somaTotal / numeroDeTermos)
print(' ')
print(f'A média é: {media}')
print(f'O menor valor é {menorValor}')
print(f'O maior valor é {maiorValor}')