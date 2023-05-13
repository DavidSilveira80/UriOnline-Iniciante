
def periodo(h_inicial, min_inicial, h_final, min_final):
    cont = min = 0
    for i in range(h_inicial, h_final):
        cont += 1
    if min_inicial < min_final:
        min = min_final - min_inicial

    return cont, min


def retorna_hora_minuto(h_inicial, min_inicial, h_final, min_final):
    if 12 < h_inicial <= 24 and 24 > h_final <= 12:
        fim = h_final + 24
        hora_min = periodo(h_inicial, fim, min_inicial, min_final)
    return hora_min


def mostrar_saida(horas, minutos):
    saida = f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)'
    return saida


hora_inicial, minuto_inicial, hora_final, minuto_final = [int(x) for x in input().split(' ')]


horas_minutos = retorna_hora_minuto(hora_inicial, minuto_inicial, hora_final, minuto_final)
print(mostrar_saida(horas_minutos[0], horas_minutos[1]))

"""minutos = 0
   if h_inicial < h_final:
       minutos = ((h_final * 60) + min_final) - ((h_inicial * 60) + min_inicial)
   elif h_inicial > h_final:
       minutos = ((h_inicial * 60) + min_inicial) - ((h_final * 60) + min_final)
   elif h_inicial == h_final and min_final > min_inicial:
       minutos = ((h_final * 60) + min_final) - ((h_inicial * 60) + min_inicial)
   """
# if minutos == 0:
# return (24, 0)
# else:
# return (minutos // 60, minutos % 60)