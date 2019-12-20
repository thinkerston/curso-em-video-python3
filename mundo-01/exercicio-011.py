'''Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua area e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta área de 2m²'''

print(' Insira a largura e altura da parede para calcular seu tamanho em m²\n e quanto de tinta é necessário para pinta-lá\n visto que 1L de tinta pinta 2m²', end='\n \n')
altura = float(input('insira a altura da parede: '))
largura = float(input('insira a largura da parede: '))
metrosQuadrados = float(altura * largura)
tintaNecessaria = float(metrosQuadrados / 2)

print(f'Para pintar {metrosQuadrados}m² é necessário {tintaNecessaria}L de tinta')