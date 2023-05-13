"""
Dados dois números inteiros, n e m, quantos dígitos tem n**m ?

Exemplos:

2 e 10 - 2**10 = 1024 - 4 dígitos

3 e 9 - 3**9 = 19683 - 5 dígitos

Entrada
A entrada é composta por vários casos de teste. A primeira linha tem um número inteiro C, representando a
quantidade de casos de teste. As C linhas seguintes contém dois números inteiros N e M (1 <= N, M <= 100).

Saída
Para cada caso de teste de entrada do seu programa, você deve imprimir um número inteiro contendo a quantidade
de dígitos do resultado da potência calculada no respectivo caso de teste.

Exemplo de Entrada	   Exemplo de Saída

4                      1
1 1                    4
2 10                   5
3 9                    201
100 100

"""


casos_de_teste = int(input())

cont = 1
while cont <= casos_de_teste:
    numeros = [int(i) for i in input().split(' ')]
    print(len(str(pow(numeros[0], numeros[1]))))
    cont += 1
