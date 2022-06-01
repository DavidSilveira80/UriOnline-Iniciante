N = int(input())
cont = 0
while cont < N:
    valores = input().split()
    x, y = int(valores[0]), int(valores[1])
    
    if y == 0:
        print('divisao impossivel')
    else:
        print(f'{x / y:.1f}')
    cont += 1