print(f'{" LANÇAMENTO DE NOTAS ":•^50}')

listaEstudantes = list()
listaDeNotas = list()
mediaNotas = list()

while True:
    listaDeNotas.append(str(input('Nome: ')).strip().capitalize())
    listaDeNotas.append(float(input('Nota 1: ')))
    listaDeNotas.append(float(input('Nota 2: ')))
    mediaNotas.append((listaDeNotas[:][1] + listaDeNotas[:][2]) / 2)
    listaEstudantes.append(listaDeNotas[:])
    listaDeNotas.clear()
    sair = str(input('Quer continuar? [S/N] ')).strip().upper()
    if sair == 'N':
        break

print(f'{" BOLETIM DA CLASSE ":-^30}')
print(f'{"Nº"}| {"NOME":^15} | {"MÉDIA":>8}')

for people in range(len(listaEstudantes)):
    print(f'{people} | {listaEstudantes[people][0]:^15} | {mediaNotas[people]:>8.1f}')

print('-' * 30)
print('•' * 50)

while True:
    nota = int(input('Mostrar notas de qual aluno?[999 to Stop] '))
    if nota != 999:
        for aluno in range(1):
            print(f'Notas de {listaEstudantes[nota][0]}: {listaEstudantes[nota][1:]}')
            print('.' * 50)
    elif nota == 999:
        break

print(f'{" VOLTE SEMPRE ":•^50}')

