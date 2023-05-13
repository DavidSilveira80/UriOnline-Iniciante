"""
Na matemática, um Número Primo é aquele que pode ser dividido somente
por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser
dividido apenas pelo número 1 e pelo número 7.

Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém
um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada.
Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

Saída
Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”,
de acordo com a especificação fornecida.

Exemplo de Entrada	   Exemplo de Saída

3
8                      8 nao eh primo
51                     51 nao eh primo
7                      7 eh primo

"""


def verifica_quantidade_de_divisores(dividendo):
    qtd_divisores = 0
    for i in range(1, dividendo + 1):
        if dividendo % i == 0:
            qtd_divisores += 1
    return qtd_divisores


def mostra_se_eh_primo(dividendo):
    qtd_divisores = verifica_quantidade_de_divisores(dividendo)
    if qtd_divisores == 2:
        saida = f'{dividendo} eh primo'
    else:
        saida = f'{dividendo} nao eh primo'
    return saida


casos_de_teste = int(input())
contador = 1

while contador <= casos_de_teste:
    dividendo = int(input())
    print(mostra_se_eh_primo(dividendo))
    contador += 1
    