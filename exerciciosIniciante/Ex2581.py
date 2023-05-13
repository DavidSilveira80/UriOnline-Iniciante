"""
oorg é o integrante mais sábio do grupo de heróis denominado Os Protetores da Via Láctea.
Para qualquer pergunta, ele tem a resposta ideal! Escreva um programa que, dada uma pergunta,
informe a resposta de Toorg.

Entrada
A entrada terá diversos casos de teste. A cada caso de teste, um número N é apresentado, que
representa o número de casos de teste. Em seguida, haverá N linhas, com as perguntas feitas para Toorg.

Saída
Para cada caso de teste, imprima a resposta de Toorg.

Exemplo de Entrada	           Exemplo de Saída

3
Who are you?                  I am Toorg!
How old are you?              I am Toorg!
What can I do for you?        I am Toorg!
"""

casos_de_teste = int(input())

cont = 1

while cont <= casos_de_teste:
    pergunta = input()
    print('I am Toorg!')
    cont += 1
