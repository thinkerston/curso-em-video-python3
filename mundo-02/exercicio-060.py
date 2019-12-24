'''faça um programa que  leia um numero qualquer e mostre o seu a fatorial'''

numero = int (input('insira um numero para ver o fatorial: '))
fatorial = int(1)
numeroOriginal = numero

while numero > 1:
    fatorial = fatorial * numero
    numero -=1

print(f'o fatorial de {numeroOriginal} é {fatorial}')