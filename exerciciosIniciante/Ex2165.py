"""
O microblog Twitter é conhecido por limitar as postagens em 140 caracteres.
 Conferir se um texto vai caber em um tuíte é sua tarefa.

Entrada
A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

Saída
A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a l
inha de texto T tem até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE".

Exemplo de Entrada	                                      Exemplo de Saída

RT @TheEllenShow: If only Bradley's arm was               TWEET
longer. Best photo ever. #oscars pic.twitter.
com/C9U5NOtGap
"""

texto = input()

if len(texto) > 140:
    print('MUTE')
else:
    print('TWEET')
