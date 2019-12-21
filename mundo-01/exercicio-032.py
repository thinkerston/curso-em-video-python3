'''Crie um algoritmo que verifique se o ano inserido pelo usuário forma um ano bissexto'''

ano = int(input('insira o ano que deseja verificar: '))

if (ano % 4) == 0:
    if (ano % 100) == 0 and (ano % 400) == 0:
        print (f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')
else:
    print(f'O ano {ano} não é bissexto')