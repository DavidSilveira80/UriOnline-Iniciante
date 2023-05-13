"""
O seu professor gostaria de fazer um programa com as seguintes características:

Crie 3 variáveis para armazenar uma frase de no máximo 100 caracteres;
Leia uma frase para a primeira variável;
Leia uma frase para a segunda variável;
Leia uma frase para a terceira variável;
Imprima a primeira variável lida no passo 2, a segunda variável lida no passo 3, a terceira variável lida no passo 4.
Não esqueça de pular linha;
Imprima a primeira variável lida no passo 3, a segunda variável lida no passo 4, a terceira variável lida no passo 2.
Não esqueça de pular linha;
Imprima a primeira variável lida no passo 4, a segunda variável lida no passo 2, a terceira variável lida no passo 3.
 Não esqueça de pular linha;

Repita o procedimento 5, imprimindo só 10 caracteres de cada variável.

Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem três linhas. Na primeira linha tem
uma variável A que armazena uma frase de no máximo 100 caracteres. Na segunda linha tem uma variável B que
armazena uma frase de no máximo 100 caracteres. Na terceira linha tem uma variável C que armazena uma frase
de no máximo 100 caracteres. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem quatro linhas da forma descrita
nos itens 5, 6, 7 e 8. Conforme mostra o exemplo de saída a seguir.


Exemplos de Entrada	        Exemplos de Saída

Roberto                     RobertoCarlosAldo
Carlos                      CarlosAldoRoberto
Aldo                        AldoRobertoCarlos
                            RobertoCarlosAldo

aaaa bbbb cccc              aaaa bbbb ccccccccxxxxx xxxx xx
cccc                        ccccxxxxx xxxx xxaaaa bbbb cccc
xxxxx xxxx xx               xxxxx xxxx xxaaaa bbbb cccccccc
                            aaaa bbbb ccccxxxxx xxxx
"""

frase1 = input()
frase2 = input()
frase3 = input()

print(f'{frase1}{frase2}{frase3}')
print(f'{frase2}{frase3}{frase1}')
print(f'{frase3}{frase1}{frase2}')
print(f'{frase1[0:10]}{frase2[0:10]}{frase3[0:10]}')
