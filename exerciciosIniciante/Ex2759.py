"""
O seu professor gostaria de fazer um programa com as seguintes características:

Crie 3 variáveis para armazenar um único carácter;
Leia um valor carácter para a primeira variável;
Leia um valor carácter para a segunda variável;
Leia um valor carácter para a terceira variável;
Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado
na primeira variável lida no passo 2, uma virgula, um espaço em branco, a letra B, um espaço em branco,
o sinal de igual, um espaço em branco, o carácter armazenado na segunda variável lida no passo 3, a letra C,
um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na terceira variável lida
no passo 4. Não esqueça de pular linha;
Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na
primeira variável lida no passo 3, uma virgula, um espaço em branco, a letra B, um espaço em branco,
o sinal de igual, um espaço em branco, o carácter armazenado na segunda variável lida no passo 4, a letra C,
 um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na terceira variável lida
  no passo 2. Não esqueça de pular linha;
Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na
primeira variável lida no passo 4, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal
 de igual, um espaço em branco, o carácter armazenado na segunda variável lida no passo 2, a letra C, um espaço
  em branco, o sinal de igual, um espaço em branco, o carácter armazenado na terceira variável lida no passo 3.
   Não esqueça de pular linha.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem três linhas. Na primeira linha tem
uma variável A que armazena um valor carácter. Na segunda linha tem uma variável B que armazena um valor carácter.
 Na terceira linha tem uma variável C que armazena um valor carácter. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem três linhas da forma
descrita nos itens 5, 6 e 7. Conforme mostra o exemplo de saída a seguir.


a
b
c

A = a, B = b, C = c
A = b, B = c, C = a
A = c, B = a, C = b

0
1
2

A = 0, B = 1, C = 2
A = 1, B = 2, C = 0
A = 2, B = 0, C = 1

"""


def gera_saida(a, b, c):
    return f'A = {a}, B = {b}, C = {c}\nA = {b}, B = {c}, C = {a}\nA = {c}, B = {a}, C = {b}'


a = input()
b = input()
c = input()

print(gera_saida(a, b, c))
