'''Faça um program que leia um numero de 0 a 9999 e mostre na tela os digitos separados
> exemplo: o numero digitado foi 1834
>Unidade: 4
>Dezena: 3
>Centena: 8
>milhar: 1
'''

numero = int(input('Insira um numero de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
