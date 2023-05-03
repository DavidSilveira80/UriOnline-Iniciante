"""
Resumindo a história até aqui, tivemos lutas com aranhas, trolls, orcs, wargs, fugidas em barris e muita
luta com o dragão Smaug. Após Smaug ser derrotado, os anões reivindicaram a Montanha Solitária e todas
suas riquezas. Porém, os humanos que vivem próximo a montanha foram os responsáveis por derrotar Smaug,
 e querem parte das riquezas também. Algumas riquezas das montanhas também pertenciam a elfos, e estes
 também querem reivindicar sua parte.

            Thorin, o anão líder da aventura, fica tomado pela cobiça ao ouro da montanha e perde a
            sanidade, travando assim uma guerra contra humanos e elfos.

            O que nenhum deles esperava era que os orcs e os wargs também estavam cobiçando a montanha,
            e aparecem de surpresa. Assim, humanos, elfos e anões (lado do bem) têm que se unir para
            combater os orcs e os wargs (lado do mal), travando assim a Batalha dos Cinco Exércitos.

Bilbo, nosso herói até aqui, se abstém dessa batalha, pois esta, tomou proporções grandes demais para
um hobbit, porém, ele consegue fazer uma estimativa de quem irá vencer. Basta, neste caso, somar a quantidade
dos exércitos de cada lado e verificar qual é o maior. Porém, Bilbo sabe que Gandalf tem um plano b caso os
exércitos de homens, elfos e anões percam ou empatem, e esse plano é chamar o exército de águias, aumentando
assim o número do exército do bem.

            Calcule para Bilbo quem irá vencer A Batalha dos Cinco Exércitos.

            Ah, e se mesmo com as águias os dois grandes exércitos empatarem, Bilbo estará lá com
            sua espada Ferroada, para destruir o último orc ou warg.

Entrada
Contém 6 inteiros, H, E, A, O, W e X, representando o número do exército de humanos, elfos, anões,
orcs, wargs e águias, respectivamente.

Saída
Se o lado do bem vencer: “Middle-earth is safe.”, se não, “Sauron has returned.”.

Exemplos de Entrada	   Exemplos de Saída

1 2 3 10 2 7            Middle-earth is safe.

1 2 3 10 2 5            Sauron has returned.

"""


def verifica_se_terra_media_esta_salva(humanos, elfos, anoes, orcs, wargs, aguias):
    lado_do_bem = humanos + elfos + anoes + aguias
    lado_do_mal = orcs + wargs
    if lado_do_bem > lado_do_mal:
        terra_media = 'Middle-earth is safe.'
    else:
        terra_media = 'Sauron has returned.'
    return terra_media


humanos, elfos, anoes, orcs, wargs, aguias = [int(x) for x in input().split(' ')]

print(verifica_se_terra_media_esta_salva(humanos, elfos, anoes, orcs, wargs, aguias))
