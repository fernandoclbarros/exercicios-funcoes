# Escreva um programa que execute uma função que receba um número informado no console como parâmetro e verifique se o número informado é primo ou não.

def analiseNumPrimo(numero):
    multiplos = 0

    for contador in range(1, numero +1):
        if numero % contador == 0:
            multiplos += 1
            
    if numero >= 1:
        if multiplos == 2:
            print(f'{numero} é um número primo')
        else:
            print(f'{numero} NÃO é um número primo')
    elif numero == 0:
        print(f'{numero} é zero')
    else:
        print(f'{numero} é negativo')

analiseNumPrimo (6)
