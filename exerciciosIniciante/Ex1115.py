"""
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no
sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será
encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida,
 conforme o exemplo.


Exemplo de Entrada	     Exemplo de Saída

2 2                      primeiro
3 -2                     quarto
-8 -1                    terceiro
-7 1                     segundo
0 2
"""


while True:
    X, Y = [int(x) for x in input().split(' ')]

    if X > 0 and Y > 0:
        print('primeiro')

    elif X < 0 and Y > 0:
        print('segundo')

    elif X < 0 and Y < 0:
        print('terceiro')

    elif X > 0 and Y < 0:
        print('quarto')

    elif X == 0 or Y == 0:
        break
