alcool = gasolina = diesel = 0

while True:

    tipo_combustivel = int(input())

    if tipo_combustivel == 1:
        alcool += 1
    elif tipo_combustivel == 2:
        gasolina += 1
    elif tipo_combustivel == 3:
        diesel += 1
    elif tipo_combustivel < 1 or tipo_combustivel > 4:
        continue
    elif tipo_combustivel == 4:
        break

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
