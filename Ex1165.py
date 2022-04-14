N = int(input())
cont = 1

while cont <= N:
    X = int(input())
    divisores = 0

    for i in range(1, X + 1):
        if X % i == 0:
            divisores += 1
    
    if divisores == 2:
        print(f'{X} eh primo')
    else:
        print(f'{X} nao eh primo')
    cont += 1
    