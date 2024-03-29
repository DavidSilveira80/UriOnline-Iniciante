"""
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem
"Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.

Exemplo de Entrada	  Exemplo de Saída

6 24                  Sao Multiplos

6 25                  Nao sao Multiplos

"""


def mostra_se_sao_multiplos(A, B):
    if A % B == 0 or B % A == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')


A, B = [int(x) for x in input().split(' ')]

mostra_se_sao_multiplos(A, B)
