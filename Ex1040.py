"""
Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente
às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para
cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ".
Se esta média for maior ou
igual a 7.0, imprima a mensagem "Aluno aprovado.".
Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.".
Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a
mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno.
Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a
média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima
a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou
"Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos
(aprovado ou reprovado após ter pego exame) apresente na última linha uma
mensagem "Media final: " seguido da média final para esse aluno.

Entrada
A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

Saída
Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser
impressas conforme a descrição do problema. Não esqueça de imprimir o enter após o final
de cada linha, caso contrário obterá "Presentation Error".


Exemplo de Entrada	     Exemplo de Saída

2.0 4.0 7.5 8.0          Media: 5.4
6.4                      Aluno em exame.
                         Nota do exame: 6.4
                         Aluno aprovado.
                         Media final: 5.9

2.0 6.5 4.0 9.0          Media: 4.8
                         Aluno reprovado.


9.0 4.0 8.5 9.0          Media: 7.3
                         Aluno aprovado.

"""


def atribuir_notas(entrada_valores):
    return float(entrada_valores[0]), float(entrada_valores[1]), float(entrada_valores[2]), float(entrada_valores[3])


def calcular_media(nota1, nota2, nota3, nota4):
    return ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4 * 1)) / (2 + 3 + 4 + 1)


def calcular_media_com_exame(media_atual, nota_exame):
    return (media_atual + nota_exame) / 2


def mostrar_resultado_aprovado_exame(media):
    if media >= 5.0:
        resultado = 'Aluno aprovado.'
    elif media <= 4.9:
        resultado = 'Aluno reprovado.'

    return resultado


notas = input().split(' ')
nota1, nota2, nota3, nota4 = atribuir_notas(notas)
media = calcular_media(nota1, nota2, nota3, nota4)

print(f'Media: {media:.1f}')
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif media <= 5.0 or media <= 6.9:
    print('Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')
    media_recuperacao = calcular_media_com_exame(media, nota_exame)
    print(mostrar_resultado_aprovado_exame(media_recuperacao))
    print(f'Media final: {media_recuperacao:.1f}')