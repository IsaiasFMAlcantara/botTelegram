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

"""
numeros = input()
numero_1, numero_2, numero_3 = map(int, numeros.split())
maiorAB = (numero_1 + numero_2 + abs(numero_1 - numero_2)) / 2
maior = int((maiorAB + numero_3 + abs(maiorAB - numero_3)) / 2)
print(f'{maior} eh o maior')


peca_1 = input()
peca_2 = input()
n1peca_1,n1peca_2,n1peca_3 = map(float, peca_1.split())
n2peca_1,n2peca_2,n2peca_3 = map(float, peca_2.split())
valor_pago = (n1peca_2*n1peca_3)+(n2peca_2*n2peca_3)
print(f'VALOR A PAGAR: R$ {valor_pago:.2f}')
"""
