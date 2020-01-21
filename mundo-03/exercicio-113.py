'''Reescreva a função leiaint() que foi feita no exercicio 104, incluindo agora 
a possibilidade da digitação de um número de tipo invalido.
aproveitando crie também a função leiaFloat() com a mesma funcionalidade'''

def leiaiInt():
    while True: 
        try:
            numero = int(input('Digite um numero inteiro: '))
        except:
            print(f'O valor digitado é Invalido')
        else:
            return(numero)

def leiaFloat():
    while True: 
        try:
            numero = float(input('Digite um numero Real: '))
        except:
            print(f'O valor digitado é Invalido')
        else:
            return(numero)
        
valorInteiro = leiaiInt()
valorFloat= leiaFloat()

print(f'O valor inteiro digitado foi {valorInteiro}')
print(f'O valor inteiro digitado foi {valorFloat}')