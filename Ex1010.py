"""
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o
valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente
dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um
espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

Exemplos de Entrada	     Exemplos de Saída

12 1 5.30                VALOR A PAGAR: R$ 15.50
16 2 5.10

13 2 15.30               VALOR A PAGAR: R$ 51.40
161 4 5.20

1 1 15.10                VALOR A PAGAR: R$ 30.20
2 1 15.10
"""

entradas_peca1 = input().split(" ")
entradas_peca2 = input().split(" ")

codigo_peca1 = int(entradas_peca1[0])
numero_de_pecas1 = int(entradas_peca1[1])
valor_unitario_peca1 = float(entradas_peca1[2])

codigo_peca2 = int(entradas_peca2[0])
numero_de_pecas2 = int(entradas_peca2[1])
valor_unitario_peca2 = float(entradas_peca2[2])

valor_total_peca1 = numero_de_pecas1 * valor_unitario_peca1
valor_total_peca2 = numero_de_pecas2 * valor_unitario_peca2

valor_total = valor_total_peca1 + valor_total_peca2

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')

