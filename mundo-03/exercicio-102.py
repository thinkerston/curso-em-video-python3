'''Crie um programa que tenha função fatorial() que receba dois parametros: 
o primeiro que indique o número a calcular e o outro chamado show, que será um valor
logico chamado show, (opcional) indicando se srerá mostrado ou não na tela 
o processo de calculo fatorial'''


def showCalculo(valor):


    for i in range(valor):
        print(f'{valor} x', end=' ')
        valor -= 1
        
        
def fatorial(valor, show = True):
    """
    Calcula o fatorial de um numero.
    :param valor: O numero a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: o valor do fatorial de um numero valor    
    """
    calculo = valor
    if show == True:
        while calculo > 0:
            
            if calculo ==1 :
                print ('1 = ', end='')
            else:
                print(f'{calculo} x', end=' ')
            calculo -= 1
    
    fator = int(1)
    while valor > 1:
        
        fator *= valor 
        valor -= 1
    
    return(fator)



bazinga = fatorial(15)
print(bazinga)