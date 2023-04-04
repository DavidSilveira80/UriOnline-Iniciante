"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer
no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas
decimais após a vírgula, segundo a fórmula:

sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))


Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
"""
from math import sqrt, pow

eixo_X_Y_1 = input().split(" ")
eixo_X_Y_2 = input().split(" ")

x1, y1 = float(eixo_X_Y_1[0]), float(eixo_X_Y_1[1])
x2, y2 = float(eixo_X_Y_2[0]), float(eixo_X_Y_2[1])

distancia = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

print(f'{distancia:.4f}')
