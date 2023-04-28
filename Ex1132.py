"""
Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de
13 entre X e Y, incluindo ambos.

Entrada
O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada,
inclusive ambos se for o caso.

Sample Input	         Sample Output

100                      13954
200

"""


def soma_nao_multiplos_de_13(numero1, numero2):
    soma_de_nao_multiplos_de_13 = 0
    for i in range(numero1, numero2 + 1):
        if i % 13 != 0:
            soma_de_nao_multiplos_de_13 += i
    return soma_de_nao_multiplos_de_13


numero1 = int(input())
numero2 = int(input())


if numero1 > numero2:
    print(soma_nao_multiplos_de_13(numero2, numero1))

else:
    print(soma_nao_multiplos_de_13(numero1, numero2))
