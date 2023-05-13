"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente,
 uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.


Exemplo de Entrada  	Exemplo de Saída

7 21 -14                -14
                         7
                         21

                         7
                         21
                        -14

-14 21 7                -14
                         7
                         21

                        -14
                        21
                        7

"""


def imprime_lista(lista):
    for i in lista:
       print(i)


entrada = [int(x) for x in input().split(' ')]
crescente = sorted(entrada)

imprime_lista(crescente)
print('')
imprime_lista(entrada)
