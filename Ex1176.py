
"""
Faça um programa que leia um valor e apresente o número de Fibonacci
correspondente a este valor lido. Lembre que os 2 primeiros elementos
 da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2
  anteriores a ele. Todos os valores de Fibonacci calculados neste
  problema devem caber em um inteiro de 64 bits sem sinal.

Entrada
A primeira linha da entrada contém um inteiro T, indicando o número de
 casos de teste. Cada caso de teste contém um único inteiro N (0 ≤ N ≤ 60),
  correspondente ao N-esimo termo da série de Fibonacci.

Saída
Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X",
onde X é o N-ésimo termo da série de Fibonacci.

Exemplo de Entrada         Exemplo de Saída

3                          Fib(0) = 0
0                          Fib(4) = 3
4                          Fib(2) = 1
2

"""


def retornar_termo_final_fibo(max):

    a, b = 0, 1
    if max == 0:
        termo_final = max
    else:
        cont = 1
        while cont <= max:
            a, b = b, a + b
            termo_final = a
            cont += 1
    return termo_final


casos_de_teste = int(input())

cont = 1
while cont <= casos_de_teste:
    max = int(input())
    print(f'Fib({max}) = {retornar_termo_final_fibo(max)}')
    cont += 1
