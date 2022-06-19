# Escreva um programa que execute uma função que multiplique todos os números de uma lista passada por parâmetro.


lista1 = [2, 3, 4, 12, 20, 52]

def multiplicaoItensLista(lista):
    totalMultiplicacao = 1
    for numero in lista:
        totalMultiplicacao *= numero
    return print((totalMultiplicacao))

multiplicaoItensLista (lista1)