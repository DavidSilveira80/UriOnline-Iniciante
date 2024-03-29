"""
Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo.
Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

Entrada
A entrada contém um número inteiro N. Este N será a quantidade de pares de
valores inteiros (X e Y) que serão lidos em seguida.

Saída
Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal,
ou “divisao impossivel” caso não seja possível efetuar o cálculo.

Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o
C e C++ gera outro inteiro. Utilize cast :)

Exemplo de Entrada	    Exemplo de Saída

3                        -1.5
3 -2                     divisao impossivel
-8 0                     0.0
0 8

"""


def informando_valores():
    return [int(x) for x in input().split(' ')]


def informa_se_divisao_eh_possivel(x, y):
    if y == 0:
        saida = 'divisao impossivel'
    else:
        saida = f'{x / y:.1f}'

    return saida


N = int(input())

cont = 0
while cont < N:
    x, y = informando_valores()
    print(informa_se_divisao_eh_possivel(x, y))
    cont += 1
