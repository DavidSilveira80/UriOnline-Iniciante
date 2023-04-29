

def retornar_termo_final_fibo(max):

    a, b = 0, 1
    if max == 0:
        termo_final = max
    else:
        cont = 1
        while cont <= max:
            a, b = b, a + b
            termo_final = a
            cont += 1
    return termo_final


casos_de_teste = int(input())

cont = 1
while cont <= casos_de_teste:
    max = int(input())
    print(f'Fib({max}) = {retornar_termo_final_fibo(max)}')
    cont += 1
