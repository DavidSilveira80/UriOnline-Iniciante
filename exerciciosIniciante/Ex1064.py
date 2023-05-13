"""
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos.
Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com
um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante.
Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve
mostrar a média dos valores positivos digitados.

Exemplo de Entrada	  Exemplo de Saída

7                     4 valores positivos
-5                    7.4
6
-3.4
4.6
12
"""


numeros_positivos = []
media = qtd_numeros_positivos = 0

cont = 1
while cont <= 6:
   numero = float(input())
   if numero > 0:
      numeros_positivos.append(numero)
      qtd_numeros_positivos += 1
   else:
      continue
   cont += 1


print(f'{qtd_numeros_positivos} valores positivos')
print(f'{sum(numeros_positivos) / qtd_numeros_positivos:.1f}')
