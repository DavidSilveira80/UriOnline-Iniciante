"""
Faça um programa que mostre os números pares entre 1 e 100, inclusive.

Entrada
Neste problema extremamente simples de repetição não há entrada.

Saída
Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.

Exemplo de Entrada	   Exemplo de Saída

                       2
                       4
                       6
                       ...
                       100
"""


def mostra_numero_par(numero):

    if numero % 2 == 0:
        return numero


for numero in range(1, 101):
    if mostra_numero_par(numero) == None:
        continue
    else:
        print(mostra_numero_par(numero))
