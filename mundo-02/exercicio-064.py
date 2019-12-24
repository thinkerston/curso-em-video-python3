'''crie um programa que leia varios numeros interios pelo teclado.
o programa só vai parar quando usuário digitar valor 999, 
que é a condição de parada. no final mostre quantos numeros foram digitados
e qual foi a soma entre eles (desconsiderando a flag)'''

numeros = int(input('insira numeros para somar e 999 para sair: '))
sair = bool(False)
somador = int(0)
numeroDeVezes = int(0)

while sair == False:
    if numeros == 999:
        sair = bool (True)
        pass
    else:
        numeros = int(input('insira numeros para somar e 999 para sair: '))
        if numeros != 999:
            numeroDeVezes += 1
            somador += numeros
        pass
print(f'A soma total da {somador}')
print(f'foram somado numeros {numeroDeVezes} vezes')