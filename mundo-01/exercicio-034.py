'''Escreva um programa que pergunte o salario de um funcionario e  
calcule o valor de seu aumento. Para salarios superiores a R$ 1250.0
calcule um aumeneto de 10%. Para inferiores ou iguais, o aumento é de 15%'''

salario = float(input('qual o seu salario? '))

if salario <= 1250.0:
    novoSalario = float ((salario * 0.15) + salario)
    print(f'O seu salario sairá de R${salario} para R${novoSalario}')
else:
    novoSalario = float ((salario * 0.10) + salario)
    print(f'O seu salario sairá de R${salario} para R${novoSalario}')
    