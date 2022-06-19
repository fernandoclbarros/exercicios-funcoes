# Escreva um programa que execute uma função que valide se o número informado é um número perfeito ou não.

def numeroPerfeito(numero):

    listaMultiplos = []
    
    for contador in range(1, numero):
        if numero % contador == 0:
            listaMultiplos.append(contador)
            somaLista = sum(listaMultiplos)

    if somaLista == numero:
        print(f'{numero} é um número perfeito')
    else:
        print(f'{numero} NÃO é um número perfeito')
            
numeroPerfeito(33550336)