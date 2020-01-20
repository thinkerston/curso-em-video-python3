'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:
- Quantidade de notas; 
- A Maior nota;
- A Menor nota;
- A Média da turma;
- A situação (opcional)
'''

def notas(*args, situacao = False):
    dados = {}
    dados['Maior Nota'] = max(args)
    dados['Menor Nota'] = min(args)
    dados['Media'] = sum(args) / len(args)
    if situacao == True:
        if dados['Media'] > 6 and dados['Media'] < 7:
            dados['Situação'] = 'Aceitavel'
            pass
        elif dados['Media'] < 6:
            dados['Situação'] = 'Pessimos'
        else:
            dados['Situação'] = 'Bom'
            pass
    return (dados)

n = notas(10, 5, 5, 3,7,5, situacao=True)
print(n)