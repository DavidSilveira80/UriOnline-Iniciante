"""
Escreva um programa que repita a leitura de uma senha até que ela seja válida.
Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida".
Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido"
 e o algoritmo encerrado. Considere que a senha correta é o valor 2002.

Entrada
A entrada é composta por vários casos de testes contendo valores inteiros.

Saída
Para cada valor lido mostre a mensagem correspondente à descrição do problema.

Exemplo de Entrada	 Exemplo de Saída

2200                 Senha Invalida
1020                 Senha Invalida
2022                 Senha Invalida
2002                 Acesso Permitido

"""

senha = '2002'

acesso = ''
while acesso != senha:
    tentativa_acesso = input()
    if tentativa_acesso == senha:
        print('Acesso Permitido')
        acesso = tentativa_acesso
    else:
        print('Senha Invalida')
