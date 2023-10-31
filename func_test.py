def soma(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1/n2

def qual_maior(n1,n2):
    if n1 == n2:
        return 'Os numero são iguais'
    elif n1 > n2:
        return f'O maior é {n1}'
    else:
        return f'O maior é {n2}'
    
def qual_menor(n1,n2):
    if n1 == n2:
        return 'Os numero são iguais'
    elif n1 > n2:
        return f'O menor é {n2}'
    else:
        return f'O menor é {n1}'