notas_validas = soma = media = 0

while True:

    notas = float(input())

    if notas >= 0 and notas <= 10:
        notas_validas += 1
        soma += notas
        if notas_validas == 2:
            break
    elif notas < 0 or notas > 10:
        print('nota invalida')
        continue

media = soma / 2
print(f'media = {media:.2f}')
