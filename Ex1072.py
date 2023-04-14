"""
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora
do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).


Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.

Exemplo de Entrada	    Exemplo de Saída

4                       2 in
14                      2 out
123
10
-25

"""


def avalia_se_numeros_esta_no_intervalo(numero):
    if numero >= 10 and numero <= 20:
        saida = True
    else:
        saida = False

    return saida


def mostrar_saida(dentro, fora):
    return f'{dentro} in\n{fora} out'


caso_de_teste = int(input())


numeros_in = numeros_out = 0
for i in range(1, caso_de_teste + 1):
    numero = int(input())
    if avalia_se_numeros_esta_no_intervalo(numero):
        numeros_in += 1
    else:
        numeros_out += 1

print(mostrar_saida(numeros_in, numeros_out))
