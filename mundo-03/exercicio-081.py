''' Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, mostre:
- Quantos números foram digitados
- A lista de valores ordenada de forma decrescente
- Se o valor 5 foi digitado e está ou não na lista'''

contador = int(0)
lista = list()
while True:
    numero = int(input('insira um numero: '))
    contador += 1
    
    lista.append(numero)
    sair = str(input('deseja sair: Y/N: ')).lower()
    while sair not in 'yn':
        sair = str(input('deseja sair: Y/N: ')).lower()
    
    if sair == 'y':
        break
    


print(f'foram digitados {contador} numeros')
lista.sort(reverse=True)
print(lista)

if 5 not in lista:
    print(f'O valor 5 não está na lista')
    pass
else:
    print('O valor 5 está na lista')
