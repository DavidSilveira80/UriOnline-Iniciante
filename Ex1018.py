"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias,
conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso
contrário seu programa apresentará a mensagem: “Presentation Error”.

Exemplo de Entrada	                Exemplo de Saída

576                                 576
                                    5 nota(s) de R$ 100,00
                                    1 nota(s) de R$ 50,00
                                    1 nota(s) de R$ 20,00
                                    0 nota(s) de R$ 10,00
                                    1 nota(s) de R$ 5,00
                                    0 nota(s) de R$ 2,00
                                    1 nota(s) de R$ 1,00

"""
dinheiro = int(input())

notas_cem = dinheiro // 100

resto_cem = dinheiro % 100

notas_cinquenta = resto_cem // 50

resto_cinquenta = resto_cem % 50

notas_vinte = resto_cinquenta // 20

resto_vinte = resto_cinquenta % 20

notas_dez = resto_vinte // 10

resto_dez = resto_vinte % 10

notas_cinco = resto_dez // 5

resto_cinco = resto_dez % 5

notas_dois = resto_cinco // 2

resto_dois = resto_cinco % 2

notas_um = resto_dois // 1

print(dinheiro)
print(f'{notas_cem} nota(s) de R$ 100,00')
print(f'{notas_cinquenta} nota(s) de R$ 50,00')
print(f'{notas_vinte} nota(s) de R$ 20,00')
print(f'{notas_dez} nota(s) de R$ 10,00')
print(f'{notas_cinco} nota(s) de R$ 5,00')
print(f'{notas_dois} nota(s) de R$ 2,00')
print(f'{notas_um} nota(s) de R$ 1,00')
