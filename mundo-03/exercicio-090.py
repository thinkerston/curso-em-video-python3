'''Faça um programa que leia o nome e média de um aluno guardando também
a situação (>7.0 aprovado) em um dicionario. no final mostre seu conteudo
da estrutura na tela'''

dados = dict()
dados['nome'] = str(input('Insira o nome do aluno: '))
dados['media'] = float(input('insira a média do aluno: '))

if dados['media'] >= 7.0:
    dados['situacao'] = 'Aprovado'
    pass
else:
    dados['situacao'] = 'Reprovado'
    pass

print(f'O nome do aluno é {dados["nome"]}')
print(f'A média é {dados["media"]}')
print(f'E a sua situação é {dados["situacao"]}')
