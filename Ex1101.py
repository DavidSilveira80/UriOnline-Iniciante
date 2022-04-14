from telnetlib import STATUS


while True:
    valor1, valor2 = input().split()
    N = int(valor1)
    M = int(valor2)
    soma = 0
    if N <= 0 or M <= 0:
        break
    elif N > M:

        for numero in range(M, N + 1):
            soma += numero
            if numero != N:
                print(f'{numero} ',end='')
            else:    
                print(f'{numero} ' + f'{soma}\n', end='')
    elif N < M:
         
         for numero in range(N, M + 1):
             soma += numero
             if numero != M:
                 print(f'{numero} ',end='')
             else:
                 print(f'{numero} ' + f'Sum={soma}\n',end='')
