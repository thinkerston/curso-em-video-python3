'''crie um programa onde o usuário digite uma expressão qualquer que use parenteses.
seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos
e fechados na ordem correta'''

expressao = str(input('insira sua expressão: '))

if expressao.count('(') - expressao.count(')') == 0:
	print('Sua expressão esta correta !')
else:
	print('Sua expressão está incorreta !')