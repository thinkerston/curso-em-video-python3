'''desenvolva um programa que pergunta a distância em km. Calcule o preço
da ássagem, cobrando R$0.50 por viagens de até 200km e R$0.45 para viagens mais longas'''

totalKm = float(input('quantos Km deseja percorrer? '))

if totalKm <= 200:
    valorCobrado = float(totalKm * 0.5)
    print(f'O valor de usa passagem é R$ {valorCobrado}')
else:
    valorCobrado = float(totalKm * 0.45)
    print(f'O valor de usa passagem é R$ {valorCobrado}')