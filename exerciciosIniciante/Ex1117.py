"""
Faça um programa que leia as notas referentes às duas avaliações de um aluno.
Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas
válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

Entrada
A entrada contém vários valores reais, positivos ou negativos. O programa deve ser
encerrado quando forem lidas duas notas válidas.

Saída
Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem
"media = " seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o ponto decimal.

Exemplo de Entrada	   Exemplo de Saída

-3.5                   nota invalida
3.5                    nota invalida
11.0                   media = 6.75
10.0

"""


def validar_notas(nota):
    if 0 <= nota <= 10:
        valida = True
    else:
        valida = False
    return valida


def calcular_media(notas_somadas):
    return notas_somadas / 2


notas_validas = soma_das_notas = 0

while True:

    notas = float(input())

    if validar_notas(notas):
        notas_validas += 1
        soma_das_notas += notas
        if notas_validas == 2:
            break
    else:
        print('nota invalida')
        continue

print(f'media = {calcular_media(soma_das_notas):.2f}')
