'''Crie um programa que leia o nome completo de uma pessoa e mostre
>O nome com todas as letras maiúsculas
>O nome com todas minúsculas
>Quantas letras tem (sem considerar os espaços)
>quantas letras tem o primeiro nome'''

nome = str(input('Insira seu nome completo: '))
print(f'{nome.upper()}')
print(f'{nome.lower()}')


nomeNotSpace = nome.split()
nomeNotSpace = ''.join(nomeNotSpace)
print(f'Seu nome {len(nomeNotSpace)} Letras')


primeiroNome = nome.split()
primeiroNome = primeiroNome[0]
print(f'O seu primeiro nome tem {len(primeiroNome)}')