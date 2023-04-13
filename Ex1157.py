"""
Ler um número inteiro N e calcular todos os seus divisores.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Escreva todos os divisores positivos de N, um valor por linha.

Exemplo de Entrada	  Exemplo de Saída

6                     1
                      2
                      3
                      6
"""


def mostra_divisores(dividendo, divisor):
    if dividendo % divisor == 0:
        return divisor


dividendo = int(input())

for divisor in range(1, dividendo + 1):
    if mostra_divisores(dividendo, divisor) == None:
        continue
    else:
        print(mostra_divisores(dividendo, divisor))
