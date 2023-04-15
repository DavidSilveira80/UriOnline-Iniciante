"""
Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir.
Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal.
Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o
primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

Entrada
O arquivo de entrada contém um valor inteiro N na primeira linha. Cada N linha a seguir
contém um caso de teste com três valores com uma casa decimal cada valor.

Saída
Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.

Exemplo de Entrada	         Exemplo de Saída

3
6.5 4.3 6.2                  5.7
5.1 4.2 8.1                  6.3
8.0 9.0 10.0                 9.3

"""


def converte_entrada(entrada):
    return float(entrada[0]), float(entrada[1]), float(entrada[2])


def calcula_media_ponderada(valor1, valor2, vallor3):
    return ((valor1 * 2) + (valor2 * 3) + (vallor3 * 5)) / (2 + 3 + 5)


casos_de_teste = int(input())

for caso_teste in range(1, casos_de_teste + 1):
    entrada = input().split(' ')
    v1, v2, v3 = converte_entrada(entrada)
    print(f'{calcula_media_ponderada(v1, v2, v3):.1f}')
