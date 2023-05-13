"""
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os
 valores fornecidos na entrada que deverá caber em um inteiro.

Exemplo de Entrada	 Exemplo de Saída

6                    5
-5

15                   13
12

12                   0
12
"""


def soma_impares(inicio, fim):
    soma = 0
    for i in range(inicio + 1, fim):
        if i % 2 != 0:
            soma += i
    return soma


saida = lambda x, y: print(soma_impares(y, x)) if(x > y) else print(soma_impares(x, y))

x = int(input())
y = int(input())

saida(x, y)
