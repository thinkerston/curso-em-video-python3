from math import sin, tan, cos, radians

'''faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo'''

anguloGraus = float(input('insira um angulos em grau: '))
anguloRadianos = radians(anguloGraus)
print(f'o seno é {sin(anguloRadianos)}')
print(f'o seu cosseno é {cos(anguloRadianos)}')
print(f'e a sua tangente é {tan(anguloRadianos)}')