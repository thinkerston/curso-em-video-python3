'''Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem ou não formar um triângulo'''

primeiraReta = float(input('Insira a Primeira reta: '))
segundaReta = float(input('Insira a Segunda reta: '))
terceiraReta = float(input('Insira a Terceira reta: '))

if (abs(segundaReta - terceiraReta) < primeiraReta) and (primeiraReta < (segundaReta + terceiraReta)):
    if (abs(primeiraReta - terceiraReta) < segundaReta) and (segundaReta < ( primeiraReta + terceiraReta)):
        if (abs(primeiraReta - segundaReta) < terceiraReta) and (terceiraReta < (primeiraReta + segundaReta)):
            print('Os seus dados formam um triângulo')
else:
    print('os seus dados não sao capazes de formar um triângulo')