"""
Na matemática, um número perfeito é um número inteiro para o qual a soma de todos os
seus divisores positivos próprios (excluindo ele mesmo) é igual ao próprio número.
Por exemplo o número 6 é perfeito, pois 1+2+3 é igual a 6. Sua tarefa é escrever um
programa que imprima se um determinado número é perfeito ou não.

Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 20),
indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um
valor inteiro X (1 ≤ X ≤ 108), que pode ser ou não, um número perfeito.

Saída
Para cada caso de teste de entrada, imprima a mensagem “X eh perfeito” ou “X nao eh perfeito”,
de acordo com a especificação fornecida.

Exemplo de Entrada	  Exemplo de Saída

3
6                     6 eh perfeito
5                     5 nao eh perfeito
28                    28 eh perfeito

"""


def soma_divisores(dividendo):
    soma_dos_divisores = 0
    for divisor in range(1, dividendo):
        if dividendo % divisor == 0:
           soma_dos_divisores += divisor

    return soma_dos_divisores


def mostra_se_eh_perfeito(dividendo):
    if soma_divisores(dividendo) == dividendo:
        saida = f'{dividendo} eh perfeito'
    else:
        saida = f'{dividendo} nao eh perfeito'
    return saida


casos_de_testes = int(input())

contador = 1
while contador <= casos_de_testes:
    dividendo = int(input())

    print(mostra_se_eh_perfeito(dividendo))

    contador += 1
         