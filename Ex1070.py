"""
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir
de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.

Exemplo de Entrada	 Exemplo de Saída

8                    9
                     11
                     13
                     15
                     17
                     19

"""

numero = int(input())
cont = 0
while cont < 6:
    if numero % 2 != 0:
        print(numero)
        cont += 1
    numero += 1
