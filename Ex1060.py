"""
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou
positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.

Exemplo de Entrada	   Exemplo de Saída

7                      4 valores positivos
-5
6
-3.4
4.6
12

"""


def avalia_se_eh_positivo(numero):
    if numero > 0:
        saida = True
    else:
        saida = False
    return saida


qtd_numeros_positivos = 0
for i in range(1, 7):
    numero = float(input())
    if avalia_se_eh_positivo(numero):
        qtd_numeros_positivos += 1

print(f'{qtd_numeros_positivos} valores positivos')
