def metade(total):
    '''Retorna a metade do valor total'''    
    return(total * 0.5)

def dobro(total):
    '''Retorna o dobro'''
    
    return(total * 2)

def aumentar (total, porcentagem = int(10)):
    '''pega o valor total e aumenta em uma porcentagem especificada
    quando não é especifica o valor é 10%
    '''
    valorFinal = total + (total * (porcentagem / 100))
    return(valorFinal)

def diminuir(total, porcentagem = 10):
    '''pega o valor total e diminui em uma porcentagem especificada
    quando não é especifica o valor é 10%
    '''
    valorFinal = total - (total * (porcentagem / 100))
    return(valorFinal)



def formatado(valor, porcentagem):
    valorMetade = metade(valor)
    valorDobro = dobro(valor)
    aumentarPorcentagem = aumentar(valor, porcentagem)
    diminuirPorcentagem = diminuir(valor, porcentagem)
    print('A metade é R${:.2f}'.format(valorMetade).replace('.', ','))
    print('A metade é R${:.2f}'.format(valorDobro).replace('.', ','))
    print('aumentando  em {:.0f}% é R${:.2f}'.format(porcentagem, aumentarPorcentagem).replace('.', ','))
    print('diminuindo  em {:.0f}% é R${:.2f}'.format(porcentagem, diminuirPorcentagem).replace('.', ','))


