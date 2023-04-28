"""
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

Exemplo de Entrada	      Exemplo de Saída

2                          34565
113                        4
45
34565
6
...
8

"""


def retorna_o_maior_numero(numeros):
    return max(numeros)


def retorna_posicao_do_maior_numero(maior_numero, numeros):
    return numeros.index(maior_numero) + 1


numeros = []

cont = 1
while cont <= 100:
    numero = int(input())
    numeros.append(numero)
    cont += 1


maior_numero = retorna_o_maior_numero(numeros)
posicao_do_maior_numero = retorna_posicao_do_maior_numero(maior_numero, numeros)

print(f'{maior_numero}\n{posicao_do_maior_numero}')
