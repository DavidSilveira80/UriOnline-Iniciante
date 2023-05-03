"""
Todo ano, Roberto gosta de escolher a sua árvore de natal, ele não deixa ninguém escolher para ele,
 pois ele acha que a árvore para ser bonita, deve satisfazer algumas condições, como altura, espessura
 e quantidade de galhos, para ele conseguir pendurar muitos enfeites nela.

Roberto quer que sua árvore tenha pelo menos 200 centímetros de altura, mas não quer que ela seja maior
do que 300 centímetros, ou a árvore não irá caber em sua casa. Quanto a espessura, ele deseja que a sua
árvore tenha um tronco com 50 centímetros de diâmetro ou mais. O número de galhos da árvore tem que ser
igual ou maior a 150.

Entrada
A primeira linha de entrada contém um inteiro N (0 < N ≤ 10000), o número de casos teste.
As N linhas seguintes contém 3 inteiros cada, h, de g (0 < a, d, g ≤ 5000), a altura da árvore em centímetros,
 o seu diâmetro em centímetros, e a quantidade de galhos da árvore.

Saída
Sua tarefa é, para cada árvore, imprimir Sim, se ela é uma árvore que Roberto pode escolher,
ou Não, se é uma árvore que ele não deve escolher.

Exemplo de Entrada	   Exemplo de Saída

8
200 60 160              Sim
150 50 200              Nao
300 85 341              Sim
110 10 50               Nao
450 90 1141             Nao
270 40 340              Nao
262 51 432              Sim
203 60 200              Sim


"""


def avalia_altura(altura):
    arvore_aprovada = lambda altura: True if(200 <= altura <= 300) else False
    return arvore_aprovada(altura)


def avalia_diametro(diametro):
    diametro_aprovado = lambda diametro: True if (diametro >= 50) else False
    return diametro_aprovado(diametro)


def avalia_galhos(galhos):
    galhos_aprovados = lambda galhos: True if(galhos >= 50) else False
    return galhos_aprovados(galhos)


def avalia_arvore(altura, diametro, galhos):
    arvore_aprovada = lambda altura, diametro, galhos: True if(altura and diametro and galhos) else False
    return arvore_aprovada(altura, diametro, galhos)


saida = lambda arvore_aprova: 'Sim' if arvore_aprovada else 'Nao'

casos_de_teste = int(input())

cont = 1
while cont <= casos_de_teste:

    altura, diametro, galhos = [int(x) for x in input().split(' ')]

    altura_aprovada, diametro_aprovado, galhos_aprovados = avalia_altura(altura), \
                                                                                avalia_diametro(diametro), \
                                                                                avalia_galhos(galhos)

    arvore_aprovada = avalia_arvore(altura_aprovada, diametro_aprovado, galhos_aprovados)

    print(saida(arvore_aprovada))
    cont += 1
