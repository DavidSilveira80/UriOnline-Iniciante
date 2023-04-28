"""
Frodo era um pequeno hobbit (pessoinhas pequenas e de pés peludos) que vivia tranquilamente no Condado,
tomando seus vários cafés da manhã recheados de muitos alimentos suculentos que a dieta de um bom hobbit proporciona.
Certo dia, seu tio Bilbo lhe entrega seu famoso anel dourado, e Gandalf, um mago muito “bacanudo”,
diz a Frodo que esse anel não era normal e que deveria ser jogado na Montanha da Perdição, para que
um grande mal fosse evitado. Para essa jornada, foi formada uma comitiva, composta de anões, elfos,
humanos, hobbits e magos.
Frodo deseja saber a quantidade de cada raça que irá com ele para a jornada. Dada uma lista das pessoas
que se alistaram, faça um relatório para Frodo da comitiva.

Entrada
A primeira linha da entrada é composta por um inteiro N(0 < N <= 10), indicando o número de pessoas
que se alistaram. Cada uma das próximas N linhas seguintes são compostas por uma cadeia de caracteres
(sem espaços e de caracteres alfanuméricos apenas) e um caractere maiúsculo, indicando, respectivamente,
 o nome e o tipo da raça do respectivo ser. Este caractere poderá ser:
● A - Para anões;
● E - Para elfos;
● H - Para humanos;
● M - Para magos;
● X - Para hobbits (X, pois todo hobbit é uma incógnita para o mundo).
Saída
Deve ser apresentado um relatório com a comitiva do Frodo, indicando em cada linha quantos seres de
cada espécie estarão na jornada, seguindo a ordem: hobbits, humanos, elfos, anões e magos.

Exemplo de Entrada	   Exemplo de Saída

9
Frodo X                4 Hobbit(s)
Gandalf M              2 Humano(s)
Pippin X               1 Elfo(s)
Sam X                  1 Anao(oes)
Aragorn H
Legolas E
Gimli A
Boromir H
Merry X

"""


def retorna_raca(entrada_nome_raca):
    raca = entrada_nome_raca.split(' ')
    return raca[1].upper()


def mostra_saida(anoes, elfos, humanos, magos, hobbits):
    return f'{hobbits} Hobbit(s)\n{humanos} Humano(s)\n{elfos} Elfo(s)\n{anoes} Anao(oes)\n{magos} Mago(s)'


anoes = elfos = humanos = magos = hobbits = 0
casos_de_teste = int(input())

cont = 1
while cont <= casos_de_teste:
    entrada_nome_raca = input()

    raca = retorna_raca(entrada_nome_raca)

    if raca == 'A':
        anoes += 1
    elif raca == 'E':
        elfos += 1
    elif raca == 'H':
        humanos += 1
    elif raca == 'M':
        magos += 1
    elif raca == 'X':
        hobbits += 1
    cont += 1

print(mostra_saida(anoes, elfos, humanos, magos, hobbits))
