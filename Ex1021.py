"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2.
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial,
conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

Exemplo de Entrada	    Exemplo de Saída

576.73                  NOTAS:
                        5 nota(s) de R$ 100.00
                        1 nota(s) de R$ 50.00
                        1 nota(s) de R$ 20.00
                        0 nota(s) de R$ 10.00
                        1 nota(s) de R$ 5.00
                        0 nota(s) de R$ 2.00
                        MOEDAS:
                        1 moeda(s) de R$ 1.00
                        1 moeda(s) de R$ 0.50
                        0 moeda(s) de R$ 0.25
                        2 moeda(s) de R$ 0.10
                        0 moeda(s) de R$ 0.05
                        3 moeda(s) de R$ 0.01

4.00                    NOTAS:
                        0 nota(s) de R$ 100.00
                        0 nota(s) de R$ 50.00
                        0 nota(s) de R$ 20.00
                        0 nota(s) de R$ 10.00
                        0 nota(s) de R$ 5.00
                        2 nota(s) de R$ 2.00
                        MOEDAS:
                        0 moeda(s) de R$ 1.00
                        0 moeda(s) de R$ 0.50
                        0 moeda(s) de R$ 0.25
                        0 moeda(s) de R$ 0.10
                        0 moeda(s) de R$ 0.05
                        0 moeda(s) de R$ 0.01

91.01                   NOTAS:
                        0 nota(s) de R$ 100.00
                        1 nota(s) de R$ 50.00
                        2 nota(s) de R$ 20.00
                        0 nota(s) de R$ 10.00
                        0 nota(s) de R$ 5.00
                        0 nota(s) de R$ 2.00
                        MOEDAS:
                        1 moeda(s) de R$ 1.00
                        0 moeda(s) de R$ 0.50
                        0 moeda(s) de R$ 0.25
                        0 moeda(s) de R$ 0.10
                        0 moeda(s) de R$ 0.05
                        1 moeda(s) de R$ 0.01

"""

dinheiro = float(input())

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

moedas_um = resto_dois // 1

resto_moedas_um = resto_dois % 1

moedas_cinquenta_cents = resto_moedas_um // 0.50

resto_moedas_cinquenta_cents = resto_moedas_um % 0.50

moedas_vinte_cinco_cents = resto_moedas_cinquenta_cents // 0.25

resto_moedas_vinte_cinco_cents = resto_moedas_cinquenta_cents % 0.25

moedas_dez_cents = resto_moedas_vinte_cinco_cents // 0.10

resto_moedas_dez_cents = resto_moedas_vinte_cinco_cents % 0.10

moedas_cinco_cents = resto_moedas_dez_cents // 0.05

resto_moedas_cinco_cents = resto_moedas_dez_cents % 0.05

moedas_um_cents = resto_moedas_cinco_cents // 0.01

print("NOTAS:")
print(f'{notas_cem:.0f} nota(s) de R$ 100.00')
print(f'{notas_cinquenta:.0f} nota(s) de R$ 50.00')
print(f'{notas_vinte:.0f} nota(s) de R$ 20.00')
print(f'{notas_dez:.0f} nota(s) de R$ 10.00')
print(f'{notas_cinco:.0f} nota(s) de R$ 5.00')
print(f'{notas_dois:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moedas_um:.0f} moeda(s) de R$ 1.00')
print(f'{moedas_cinquenta_cents:.0f} moeda(s) de R$ 0.50')
print(f'{moedas_vinte_cinco_cents:.0f} moeda(s) de R$ 0.25')
print(f'{moedas_dez_cents:.0f} moeda(s) de R$ 0.10')
print(f'{moedas_cinco_cents:.0f} moeda(s) de R$ 0.05')
print(f'{moedas_um_cents:.0f} moeda(s) de R$ 0.01')
