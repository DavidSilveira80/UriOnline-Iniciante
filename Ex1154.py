"""
Faça um algoritmo para ler um número indeterminado de dados, contendo cada um,
a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o
valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

Entrada
A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando
um valor negativo for lido.

Saída
A saída contém um valor correspondente à média de idade dos indivíduos.

A média deve ser impressa com dois dígitos após o ponto decimal.

Exemplo de Entrada	         Exemplo de Saída

34                           39.25
56
44
23
-2

"""


soma_idades_individuos = []
media_idades = qtd_individuos = 0


def calcula_media_das_idades(soma_idades, numero_individuos):
    return sum(soma_idades) / numero_individuos


while True:
    idades_individuos = int(input())

    if idades_individuos < 0:
        break
    else:
        soma_idades_individuos.append(idades_individuos)
        qtd_individuos += 1

media_idades = calcula_media_das_idades(soma_idades_individuos, qtd_individuos)
print(f'{media_idades:.2f}')
