'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
no final mostre:
- A média de idade do grupo;
- qual o nome do homem mais velho.
- quantas mulheres tem menos de 21 anos'''

homemMaisVelho = []
idadeHomemVelho = int(0)
somaIdade = int(0)
mulherMenorVinteAnos = int(0)
numeroElementos = int(0)


for i in range(0, 4):
    nome = str(input('Insira seu nome: '))
    idade = int(input('insira sua idade: '))
    sexo = str(input('insira seu Sexo [M] ou [F]: ')).lower()
    
    somaIdade += idade
    
    if (sexo == 'm') and (idade > idadeHomemVelho):
        homemMaisVelho = nome
    if (sexo == 'f') and (idade < 20):
        mulherMenorVinteAnos += 1
    print('//--'*8)
    numeroElementos += 1
    
mediaIdade = float(somaIdade / numeroElementos)
print(f'A media de idade é: {mediaIdade}')
print(f'O nome do homem mais velho é: {homemMaisVelho}')
print(f'O numero de mulheres menos de 20 anos é: {mulherMenorVinteAnos}')