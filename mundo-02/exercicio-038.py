'''Escreva um progaram que leia dois numeros inteiros e compare-os
mostrando na tela a seguinte mensagem: 
- o Primeiro valor é maior;
- O segundo valor é maior;
- Não existe valor maior, os dois sao iguais.'''

primeiroNumero = int(input('Insira o primeiro numero: '))
segundoNumero = int(input('Insira o segundo numero: '))

if primeiroNumero > segundoNumero:
    print('o primeiro é maior')
    pass
elif primeiroNumero < segundoNumero:
    print('O segundo numero é o maior')
    pass
else:
    print('Não existe numero maior os dois são iguais')
    pass