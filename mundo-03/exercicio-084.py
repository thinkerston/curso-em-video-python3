'''faça um programa que leia nome e peso de várias pessoas guardando tudo em uma 
lista. No final mostre:
- Quantas pessoas foram cadastradas;
- Uma listagem com as pessoas mais pesadas;
- Uma listagem com as pessoas mais leves.'''

pessoas = list()
maiorPeso = int(0)
menorPeso = int(0)
nomeMenorPeso = list()
nomeMaiorPeso = list()
contador = int(0)
primeiro = bool(True)

while True:
    nome = str(input('Insira um nome: '))
    peso = float(input('Insira um peso: '))
    pessoas.append([nome, peso])
    sair = str(input('Deseja sair? Y/N')).lower()
    while sair not in 'yn':
        sair = str(input('Deseja sair? Y/N')).lower()
    if sair == 'y':
        break
    contador+= 1

for pessoa in pessoas:
    
    if primeiro == True:
        maiorPeso = pessoa[-1]
        menorPeso = pessoa[-1]
        primeiro = bool(False)
    if pessoa[-1] < menorPeso:
        menorPeso = pessoa[-1]
        nomeMenorPeso.clear()
        nomeMenorPeso.append(pessoa[0])
        pass
    if (pessoa[-1] == menorPeso) and (pessoa[0] not in nomeMenorPeso):
        nomeMenorPeso.append(pessoa[0])
    
    if pessoa[-1] > maiorPeso:
        maiorPeso = pessoa[-1]
        nomeMaiorPeso.clear()
        nomeMaiorPeso.append(pessoa[0])
        pass
    if (pessoa[-1] == maiorPeso) and (pessoa[0] not in nomeMaiorPeso):
        nomeMaiorPeso.append(pessoa[0])
    
print(f'Foram cadastrados {contador} pessoas')
print(f'A pessoa mais leve pesa {menorPeso} kg e é {nomeMenorPeso}')
print(f'A pessoa mais pesada tem {maiorPeso} kg e é {nomeMaiorPeso}')