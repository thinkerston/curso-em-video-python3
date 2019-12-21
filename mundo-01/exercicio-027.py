'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

nomeCompleto = str(input('Insira seu nome completo: '))
nomeSplit = nomeCompleto.split()
print(f'seu primeiro nome é: {nomeSplit[0]}')
print(f'seu ultimo nome é: {nomeSplit[-1]}')