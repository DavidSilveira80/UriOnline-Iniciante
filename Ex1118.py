flag = 1
soma = media = notas_validas = 0

while flag == 1:
    notas = float(input())

    if notas >= 0 and notas <= 10:
        soma += notas
        notas_validas += 1

        if notas_validas == 2:
            media = soma / 2
            print(f'media = {media:.2f}')
            media = soma = notas_validas = 0
            print('novo calculo (1-sim 2-nao)')
            flag = int(input())

            while flag != 1 and flag != 2:
                print('novo calculo (1-sim 2-nao)')
                flag = int(input())
    else:
        print('nota invalida')
        