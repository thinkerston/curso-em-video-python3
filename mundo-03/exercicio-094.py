'''Crie um programa que leia nome, sexo e idade de várias pessoas
, guardando
os dados de cada pessoas em um dicionario e todos os dicionários em uma. no final
mostre:
- Quantas pessoas
 foram cadastradas;
- A média de idade do grupo;
- Uma lista com todas as mulheres;
- Uma lista com todas as pessoas
 acima da média.'''

pessoa = dict()
grupo = []
mediaIdade = int(0)
somaIdade = int(0)
pessoasAcimaMediaIdade = []

while True:
    
    pessoa['nome'] = str(input('Insira seu nome: '))
    pessoa['sexo'] = str(input('Insira seu sexo M/F: ')).lower().strip()
    pessoa['idade'] = int(input('Insira sua idade: '))
    grupo.append(pessoa.copy())
    somaIdade += pessoa['idade']
    sair = str(input('Deseja sair? Y/N: ')).lower()
    while sair not in 'yn':
        sair = str(input('Deseja sair? Y/N: ')).lower()
    if sair == 'y':
        break
    
mediaIdade = (somaIdade / (len(grupo)))

listaMulheres = []
for i in grupo:
    somaIdade += i['idade']
    if i['sexo'] == 'f':
        listaMulheres.append(i['nome'])
        pass
    if i['idade'] > mediaIdade:
        pessoasAcimaMediaIdade.append(i)
        pass

print('========'*8)
print(f'O grupo tem {len(grupo)} pessoas cadastradas')
print(f'A Media de idade é de {mediaIdade}')
print(f'As Mulheres cadastradas foram {listaMulheres}')
for k in pessoasAcimaMediaIdade:
    print(f'nome = {k["nome"]}; sexo = {k["sexo"]}; idade = {k["idade"]}')