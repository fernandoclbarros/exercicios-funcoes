# Escreva um programa que execute uma função que conte o número de letras maiúsculas e minúsculas de um texto e que ao final, chame outra função para imprimir o resultado.

def contagemMaiusculasMin(texto):
    maiusculas = 0
    minusculas = 0

    for letra in texto:
        if letra.isupper():
            maiusculas += 1
        elif letra.islower():
            minusculas += 1
    return print(imprimirResultado(maiusculas, minusculas))


def imprimirResultado(maiusculas, minusculas):
    print(f'O texto contém {maiusculas} letras maiúsculas e {minusculas} letras minúsculas')


textoTeste = 'Aprendendo programação em Python na DB1 Start!'

contagemMaiusculasMin (textoTeste)