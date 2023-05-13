X = int(input())
cont = 0
multiplos = 0
lista = []

while True:
    cont += 1
    lista.append(cont)

    if cont % 4 == 0:
        multiplos += 1

    if multiplos == X:
        break

for i in range(len(lista)):
    if lista[i] % 4 == 0:
        lista[i] = 'PUM'

    if lista[i] != 'PUM':
        print(f'{lista[i]} ',end='')
    else:
        print(f'{lista[i]}\n',end='')