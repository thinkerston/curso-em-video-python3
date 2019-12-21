'''Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
a multa vai custar R$7.00 para cada km acima do limite'''

velocidade = float(input('Quanto km/h o seu carro está? '))

if velocidade > 80.0:
    valorMulta = float((velocidade - 80.0) * 7)
    print('Meus pesames vc foi multado')
    print(f'devera pagar R${valorMulta:.2f} para o Estado')
else:
    print('Segue a vida companheiro')