"""
Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida.
Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN),
ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0),
embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá
imprimir apenas NULL.

Entrada
A primeira linha da entrada contém um valor inteiro N(N < 10000) que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).

Saída
Para cada caso, imprima uma mensagem correspondente, de acordo com o exemplo abaixo. Todas as letras
deverão ser maiúsculas e sempre deverá haver um espaço entre duas palavras impressas na mesma linha.

Exemplo de Entrada	    Exemplo de Saída

4
-5                      ODD NEGATIVE
0                       NULL
3                       ODD POSITIVE
-4                      EVEN NEGATIVE

"""


def avalia_par_impar(numero):
    if numero < 0 and numero % 2 == 0:
        saida = 'EVEN NEGATIVE'
    elif numero < 0 and numero % 2 != 0:
        saida = 'ODD NEGATIVE'
    elif numero > 0 and numero % 2 == 0:
        saida = 'EVEN POSITIVE'
    elif numero > 0 and numero % 2 != 0:
        saida = 'ODD POSITIVE'
    elif numero == 0:
        saida = 'NULL'
    return saida


caso_de_testes = int(input())

cont = 1
while cont <= caso_de_testes:
    numero = int(input())
    print(avalia_par_impar(numero))
    cont += 1
