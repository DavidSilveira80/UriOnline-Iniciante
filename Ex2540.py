"""
Analógimôn Go! é um jogo bastante popular. Os jogadores de Analógimôn Go!
são divididos em três grandes times: Time Valor, Time Instinto e Time Místico,
que são liderados pelos seus líderes Kandera, Esparky e Blanque, respectivamente.
Naturalmente, você faz parte de um desses times!

O líder do seu time está sendo acusado de infringir as regras do jogo por gerenciar
incorretamente os doces recebidos do Professor que são destinados ao time. Isto criou
uma grande polêmica dentro da equipe: alguns jogadores defendem que o líder realmente
agiu incorretamente e deve sofrer um impeachment e ser afastado de seu cargo, enquanto
outros defendem que ele não infringiu as regras, que a acusação é inverídica e que ele
deve continuar no cargo.

Para resolver a situação, uma votação será realizada entre todos os N jogadores do seu time.
Cada jogador deverá votar se o impeachment deve ou não ocorrer.
Se o número de votos favoráveis ao impeachment foi maior ou igual a 2/3 (dois terços) do total de jogadores,
o líder será afastado.
Caso contrário, a acusação é arquivada e ele continuará no cargo.

Dados os votos de todos os jogadores, determine o resultado da votação.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso contém o
inteiro N (1 ≤ N ≤ 105), o número de jogadores em seu time. A próxima linha contém
 N inteiros v1, ..., vN (vi = 0 ou 1), indicando os votos dos jogadores.
 O valor 1 indica um voto favorável ao impeachment, enquanto o valor 0 indica um voto contrário ao mesmo.

A entrada termina com fim-de-arquivo (EOF).

Saída
Para cada caso de teste, imprima uma linha contendo a palavra impeachment se o
líder deve ser afastado de seu cargo, ou acusacao arquivada caso contrário.


Exemplo de Entrada	        Exemplo de Saída

6
1 0 1 1 0 1                 impeachment
5                           acusacao arquivada
0 1 1 1 0

votacao1 = '1 0 1 1 0 1'.split(' ')
votacao2 = '0 1 1 1 0'.split(' ')

"""


def transforma_votos_em_inteiros(entradas_votos):
    votos_inteiros = []
    for voto in entradas_votos:
        votos_inteiros.append(int(voto))
    return votos_inteiros


def verifica_se_impeachment(votos, numero_votantes):
    return sum(votos) >= ((numero_votantes * 2) / 3)


def mostra_resultado(votos, votantes):
    if verifica_se_impeachment(transforma_votos_em_inteiros(votos), votantes):
        resultado = 'impeachment'
    else:
        resultado = 'acusacao arquivada'
    return resultado


while True:
    try:
        votantes = int(input())
        votos = input().split(' ')

        print(mostra_resultado(votos, votantes))

    except EOFError:
        break