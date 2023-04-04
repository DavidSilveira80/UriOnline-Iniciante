"""
Faça um programa que leia três valores e apresente o maior dos três valores lidos
seguido da mensagem “eh o maior”.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

Exemplos de Entrada	      Exemplos de Saída

7 14 106                   106 eh o maior

217 14 6                   217 eh o maior

"""

entrada_numeros = input().split(" ")

numeros = [int(entrada_numeros[0]), int(entrada_numeros[1]), int(entrada_numeros[2])]

print(f'{max(numeros)} eh o maior')
