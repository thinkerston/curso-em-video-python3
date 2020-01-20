def metade(total):
    '''Retorna a metade do valor total'''
    
    valorFinal = total / 2
    return('R${:.2f}'.format(valorFinal).replace('.', ','))

def dobro(total):
    '''Retorna o dobro'''
    valorFinal = total * 2
    return('R${:.2f}'.format(valorFinal).replace('.', ','))

def aumentar (total, porcentagem = int(10)):
    '''pega o valor total e aumenta em uma porcentagem especificada
    quando não é especifica o valor é 10%
    '''
    valorFinal = total + (total * (porcentagem / 100))
    return(('R${:.2f}'.format(valorFinal).replace('.', ',')))

def diminuir(total, porcentagem = 10):
    '''pega o valor total e diminui em uma porcentagem especificada
    quando não é especifica o valor é 10%
    '''
    valorFinal = total - (total * (porcentagem / 100))
    return('R${:.2f}'.format(valorFinal).replace('.', ','))


