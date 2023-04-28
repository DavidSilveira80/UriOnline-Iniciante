"""
A fim de parar a greve geral dos estudantes, o governo realizou uma reunião com a UFSC. Durante a
reunião a UFSC expos todos os gastos necessários para manter o funcionamento até o final do ano e o
Governo informou valores que poderia oferecer para cobrir esses gastos. A reunião não foi muito organizada,
e vários valores individuais foram mencionados, de forma que ninguém sabe se os valores oferecidos são
suficientes para cobrir todos os gastos da universidade.

Dada a lista de valores citados na reunião, sua tarefa será somas os gastos e as verbas oferecidas para
informar os estudantes da UFSC se a greve deve parar ou não.

Entrada
A entrada inicia com um inteiro N (1
≤
 N
≤
 100.000) que indica o número de valores citados na reunião. Cada linha possui um caráter T e um inteiro C (1
≤
 C
≤
 100.000) separados por um espaço em branco. T será igual a 'V' se o valor C representa uma verba
 oferecida pelo governo, ou igual a 'G' se o valor C representa um gasto da universidade.

Saída
Imprima “A greve vai parar.” caso os valores oferecidos pelo governo sejam suficientes para cobrir todos
os gastos da universidade até o final do ano, ou imprima “NAO VAI TER CORTE, VAI TER LUTA!” caso contrário.
 (Em ambos os casos a frase deve ser impressa sem aspas).


Exemplo de Entrada	   Exemplo de Saída

5
G 10                   NAO VAI TER CORTE, VAI TER LUTA!
V 20
G 10
G 100
V 30

"""


def trata_entrada(entrada):
    caracter_valor = entrada.split(' ')
    return caracter_valor[0].upper(), int(caracter_valor[1])


def calcula_valores(verba_oferecida_pelo_governo, gasto_da_universidade):
    if verba_oferecida_pelo_governo >= gasto_da_universidade:
        saida = 'A greve vai parar.'
    else:
        saida = 'NAO VAI TER CORTE, VAI TER LUTA!'

    return saida


verba_oferecida_pelo_governo = gasto_da_universidade = 0

ciclos = int(input())

cont = 1
while cont <= ciclos:
    entrada = input()
    gasto_verba = trata_entrada(entrada)

    if gasto_verba[0] == 'G':
        gasto_da_universidade += gasto_verba[1]
    elif gasto_verba[0] == 'V':
        verba_oferecida_pelo_governo += gasto_verba[1]
    ciclos += 1

print(calcula_valores(verba_oferecida_pelo_governo, gasto_da_universidade))
