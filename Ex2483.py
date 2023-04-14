"""
Você fica tão feliz no natal que tem vontade de gritar para
todo mundo: "Feliz natal!!". Pra colocar toda essa felicidade pra fora,
você montou um programa que, colocado um índice I de felicidade, seu grito de natal é mais animado.

Entrada
A entrada é composta por um inteiro I (1 < I ≤ 104) que representa o índice de felicidade.

Saída
A saída é composta pela frase "Feliz natal!", sendo repetidas I vezes a última letra a da frase.
 Uma quebra de linha é necessária após a impressão da frase.

Exemplo de Entrada	    Exemplo de Saída

 5                      Feliz nataaaaal!

"""


def concatenar_frase(letra_a):
    return 'Feliz nat'+letra_a+'l!'


numero = int(input())

letra_a = 'a' * numero

print(concatenar_frase(letra_a))
