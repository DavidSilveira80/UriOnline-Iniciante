"""
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B
pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo,
com um espaço em branco antes e depois da igualdade.


Exemplos de Entrada	   Exemplos de Saída


5                      DIFERENCA = -26
6
7
8


0                      DIFERENCA = -56
0
7
8


5                     DIFERENCA = 86
6
-7
8

"""

numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
numero4 = int(input())

diferenca = ((numero1 * numero2) - (numero3 * numero4))

print(f'DIFERENCA = {diferenca}')
