"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados
foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha
após cada uma.


Exemplo de Entrada	      Exemplo de Saída

-5                        3 valor(es) par(es)
0                         2 valor(es) impar(es)
-3                        1 valor(es) positivo(s)
-4                        3 valor(es) negativo(s)
12

"""

valores_pares = valores_impares = valores_positivos = valores_negativos = 0

cont = 1
while cont <= 5:
    numero = int(input())
    if numero < 0:
        valores_negativos += 1
    if numero > 0:
        valores_positivos += 1
    if numero % 2 != 0:
        valores_impares += 1
    if numero % 2 == 0:
        valores_pares += 1
    cont += 1

print(f'{valores_pares} valor(es) par(es)\n{valores_impares} valor(es) impar(es)\n{valores_positivos} '
      f'valor(es) positivo(s)\n{valores_negativos} valor(es) negativo(s)')
