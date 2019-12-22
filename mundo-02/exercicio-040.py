'''Crie um program que leia duas notas de um aluno e calcule sua media, 
nostrando uma mensagem final, de acordo com a média atingida:

- Média abaixo de 5.0: reprovado;
- Média entre  5.0 e 6.9: recuperação:
- Media 7.0 ou superior: aprovado'''

primeiraNota = float(input('Insira sua primeira nota: '))
segundaNota = float(input('Insira sua segunda nota: '))
media = float((primeiraNota + segundaNota) / 2)

print(f'sua media foi {media:.2f}')
if (media < 5.0):
    print('Parabens VOCÊ ESTA REPROVADO')
    pass
elif (media >= 5.0) and (media <= 6.9):
    print('Meus pesames você está de recuperação')
else:
    print('jovem, você está aprovado')
    pass