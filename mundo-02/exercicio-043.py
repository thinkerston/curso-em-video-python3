'''Desenvolva um programa logico que leia o peso e altura de uma pessoa e calcule
o seu IMC e mostre o seu status de acordo com os dados abaixo:
- abaixo de 18.5: Abaixo do peso;
- entre 18.5 e 25: peso ideal;
- 25 até 30: sobrepeso;
- 30 até 40: obesidade;
- acima de 40: obesidade morbida.'''

altura = float(input('informe sua altura (use . para separar metros de centimetros): '))
peso = float(input('informe seu peso (use . para separar kilos de gramas): '))

imc = float(peso / (altura**2))

if imc < 18.5:
    print('você está abaixo do peso!! COMA MAIS')
    pass
elif (imc >= 18.5) and (imc <= 25):
    print('parabens você teoricamente está no peso ideal')
    pass
elif (imc > 25) and (imc <= 30):
    print('Você está levemente acima do peso! faça exercicios de vez enquando')
    pass
elif (imc > 30) and (imc <= 40):
    print('Você está com OBESIDADE!! PROCURE FAZER EXERCICIOS REGULARMENTE')
    pass
else:
    print('OBESIDADE MORBIDA || PROCURE AUXILIO EMEDIATAMENTE')
