'''Faça um algoritmo que leia o salário de um fincionario e mostre seu novo salário, com 15% de aumento'''

salario = float(input('Qual o seu salario? '))
aumentoSalario = float(salario + (salario * 0.15))

print(f'O salario aumentado é R$:{aumentoSalario}')