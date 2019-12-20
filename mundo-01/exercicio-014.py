'''Crie um programa que leia temperaturas em °C e converta para fahrenheit e Kelvin'''

grausCelsius = float(input('informe a temperatura em °C: '))

fahrenheit = float((grausCelsius * 9/5) + 32)
kelvin = float(grausCelsius + 273.15)

print(f'{grausCelsius}°C em fahrenheit é {fahrenheit}')
print(f'{grausCelsius}°C em Kelvin é {kelvin}')