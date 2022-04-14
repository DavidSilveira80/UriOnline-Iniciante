individuos = soma_idades = media_idades = 0

while True:

    idade = int(input())

    if idade < 0:
        break
    else:
        soma_idades += idade
        individuos += 1

media_idades = soma_idades / individuos
print(f'{media_idades:.2f}')
