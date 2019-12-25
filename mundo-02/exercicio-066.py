'''crie um programa que leia varios numeros interios pelo teclado.
o programa só vai parar quando usuário digitar valor 999, 
que é a condição de parada. no final mostre quantos numeros foram digitados
e qual foi a soma entre eles (desconsiderando a flag)'''

somador = int(0)
numeroDeVezes = int(0)

while True:
    numeros = int(input('insira numeros para somar e 999 para sair: '))
    if numeros == 999:
        break
    pass
    
    if numeros != 999:
        numeroDeVezes += 1
        somador += numeros
    pass
print(f'A soma total da {somador}')
print(f'foram somado numeros {numeroDeVezes} vezes')