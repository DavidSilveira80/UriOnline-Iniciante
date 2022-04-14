N = int(input())
cont = 1

while cont <= N:
    X = int(input())
    soma = 0

    for divisor in range(1, X):
        if X % divisor == 0:
            soma += divisor

    if soma == X:
        print(f'{X} eh perfeito')
    else:
        print(f'{X} nao eh perfeito')
    cont += 1
         