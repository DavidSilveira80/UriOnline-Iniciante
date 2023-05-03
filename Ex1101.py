"""
Leia um conjunto não determinado de pares de valores
M e N (parar quando algum dos valores for menor ou igual a zero).
Para cada par lido, mostre a sequência do menor até o maior e a
soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N.
A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

Exemplo de Entrada	   Exemplo de Saída

5 2                    2 3 4 5 Sum=14
6 3                    3 4 5 6 Sum=18
5 0

"""


def informando_valores():
    return [int(x) for x in input().split(' ')]


def gera_sequencia(N, M):
    saida = []
    if N > M:
        for numero in range(M, N + 1):
            saida.append(numero)
    else:
        for numero in range(N, M + 1):
            saida.append(numero)
    return saida


def converter_sequencia_para_string(sequencia_inteira):
    sequencia_string = []
    for inteiro in sequencia_inteira:
        sequencia_string.append(str(inteiro))
    return sequencia_string


def gera_saida(sequencia_string, sequencia_inteira):
    seq = ' '.join(sequencia_string)
    return seq + f' Sum={sum(sequencia_inteira)}'


while True:
    N, M = informando_valores()
    soma = 0
    if N <= 0 or M <= 0:
        break
    else:
        sequencia_inteira = gera_sequencia(N, M)
        sequencia_string = converter_sequencia_para_string(sequencia_inteira)
        print(gera_saida(sequencia_string, sequencia_inteira))
