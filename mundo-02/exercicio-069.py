'''Crie um programa que leia a idade e o sexo de varias pessoas. a cada pessoa 
cadastrada, o programa deverá perguntar  se o usuário quer ou não continuar.
No final mostre:
- Quantas pessoas tem mais de 18 anos;
- Quantos homens foram cadastrados;
- quantas mulheres tem menos de 20 anos.'''

maiorDeDezoito = int(0)
homensCadastrados = int(0)
mulherMaiorVinte = int(0)

while True:
    
    while True:
        sexo = str(input('insira o sexo [M] masculino [F] femino: ')).lower()
        if sexo in 'fm':
            break
        
    
    idade = int(input('insira a idade: '))
    
    if (idade > 18):
        maiorDeDezoito += 1
        pass
    if (sexo == 'm'):
        homensCadastrados += 1
        pass
    if (sexo == 'f') and (idade < 20):
        mulherMaiorVinte += 1
        pass
    cadastrarMais = str(input('Deseja cadastrar mais [Y/N]: ')).lower()
    while cadastrarMais not in 'yn':
        cadastrarMais = str(input('Deseja cadastrar mais [Y/N]: ')).lower()
    if cadastrarMais == 'n':
        break
    print('======' * 15)

print(f'{maiorDeDezoito} cadastrados tem mais de 18 anos ')
print(f'{homensCadastrados} homens foram cadastrados')
print(f'{mulherMaiorVinte} mulheres em menos de 20 anos')