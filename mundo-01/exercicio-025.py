'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

nomePessoa = str(input('Insira seu nome completo e verificarei se tem "Silva": ')).lower()
temSilva = bool('silva' in nomePessoa)
print(temSilva)