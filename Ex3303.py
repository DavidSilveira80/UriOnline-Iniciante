"""
Recentemente Juquinha aprendeu a falar palavrões. Espantada com a descoberta do garoto,
sua mãe o proibiu de falar qualquer palavrão, sobre o risco de o menino perder sua mesada.

Como Juquinha odeia ficar sem mesada, ele te contratou para desenvolver um programa que informe
 para ele se uma palavra é um palavrão ou não.

Palavrões são palavras que contém dez ou mais caracteres, todas as outras palavras são consideradas palavrinhas.

Entrada
A entrada consiste em vários casos de teste. Cada caso contém uma string que descreve a palavra
 que Juquinha deseja consultar. Essa string é composta apenas de letras minúsculas e seu tamanho
 não excede 20 caracteres.

Saída
Para cada caso de teste imprima se a palavra que Juquinha consultou é um palavrão ou uma palavrinha.

Exemplos de Entrada	    Exemplos de Saída

paralelepipedo          palavrao

carro                   palavrinha
"""

while True:
    try:
        palavra = input()
        if len(palavra) >= 10:
            print('palavrao')
        else:
            print('palavrinha')
    except EOFError:
        break
