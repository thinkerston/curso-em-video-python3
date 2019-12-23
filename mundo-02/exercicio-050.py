'''Desenvolva um numero que leia 6 numeros inteiros e mostre a soma apenas
daqueles que forem pares. se algum valor digitado for impar desconsidere-o'''

print('irei somar numeros pares que vc inserir')

soma = int(0)
for i in range (0, 6):
    numero = int(input('Insira o numero: '))
    if (numero % 2 == 0):
        soma += numero

print(f'A soma dos numeros é {soma}')