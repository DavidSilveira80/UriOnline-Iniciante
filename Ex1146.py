while True:
    x = int(input())
    cont = 1
    while cont <= x:
        if cont == x:
            print(f'{cont}',end='' + '\n')
        else:
            print(f'{cont}' + " ",end="")
        cont += 1
    if x == 0:
        break
    else:
        continue
    