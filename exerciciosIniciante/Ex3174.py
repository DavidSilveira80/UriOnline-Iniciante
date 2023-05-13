"""
Todo ano, Papai Noel faz o recrutamento de elfos e gnomos para a sua equipe de preparação natalina.
 O setor de sua produção que mais tem alterações ao longo do ano é o da fabricação dos presentes,
 pois ele contrata elfos temporários, que trabalham uma determinada quantidade de horas H com ele.
 Além disso, cada elfo é contratado para um dos 4 diferentes grupos de trabalho, onde cada um dos
 grupos possui uma quantidade de horas para produzir os presentes do tipo do grupo:

Grupo dos bonecos: 8 horas;
Grupo dos arquitetos: 4 horas;
Grupo dos musicos: 6 horas;
Grupo dos desenhistas: 12 horas.

Note que os trabalhadores do grupo dos bonecos só produzem bonecos, o dos arquitetos, casas,
e assim sucessivamente. Mas cada tipo de presente conta como um presente completo no final do dia.

O Papai Noel possui uma lista dos nomes dos elfos escolhidos esse ano, com a quantidade de horas
e em que grupo que eles podem trabalhar. Sabendo da sua habilidade com programação, o Noel quer
uma forcinha sua para dizer para ele quantos presentes ele vai conseguir ter pronto, por dia, de
acordo com a quantidade de elfos que ele contratou.

Entrada
O primeiro valor da entrada é um valor inteiro N (1 ≤ N ≤ 1000), indicando a quantidade de elfos
que o Papai Noel contratou. As N linhas seguintes possuem três valores E, G e H (1 ≤ H ≤ 24),
indicando respectivamente o nome do elfo, em qual grupo ele vai trabalhar (em letras minúsculas) e
quantas horas por dia ele irá ajudar (em valor inteiro).

Saída
A saída deverá ser um inteiro P, a quantidade total de presentes produzida por dia pela fábrica do Papai Noel.

Exemplo de Entrada	              Exemplo de Saída

7
Aradhel bonecos 10
Aerin arquitetos 15
Anna musicos 10
Elbereth musicos 10
Freda desenhistas 15
Arwen bonecos 10
Logolas bonecos 10

"""


def retorna_grupo_hora(nome_grupo_hora):
    return nome_grupo_hora[1], int(nome_grupo_hora[2])


def calcula_qtd_presentes_por_dia(bonecos_ht, arquitetos_ht, musicos_ht, desenhistas_ht):
    return (bonecos_ht // 8) + (arquitetos_ht // 4) + (musicos_ht // 6) + (desenhistas_ht // 12)


bonecos_ht = arquitetos_ht = musicos_ht = desenhistas_ht = 0
elfos = int(input())

cont = 1
while cont <= elfos:
    nome_grupo_horas = input().split(' ')
    grupo_hora = retorna_grupo_hora(nome_grupo_horas)

    if grupo_hora[0] == 'bonecos':
        bonecos_ht += grupo_hora[1]
    elif grupo_hora[0] == 'arquitetos':
        arquitetos_ht += grupo_hora[1]
    elif grupo_hora[0] == 'musicos':
        musicos_ht += grupo_hora[1]
    elif grupo_hora[0] == 'desenhistas':
        desenhistas_ht += grupo_hora[1]
    cont += 1

print(calcula_qtd_presentes_por_dia(bonecos_ht, arquitetos_ht, musicos_ht, desenhistas_ht))
