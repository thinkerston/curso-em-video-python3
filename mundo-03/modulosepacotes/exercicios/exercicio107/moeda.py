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


