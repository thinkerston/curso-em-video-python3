'''Crie um programa que leia o nome de uma cidade e diga se ala começa ou não com o nome SANTO'''

nomeCidade = str(input('Insira o nome de sua cidade: ')).lower()
santoExiste = bool('santo' in nomeCidade)
print(santoExiste)