array1 = [[], [], [], [], [], [], [], [], [], [], [], []]

index = 0
soma_coluna = 0

C = int(input())
T = input().upper()

while True:
    x = float(input())
    array1[index].append(x)
    
    if len(array1[index]) == 12:
        index += 1
    else:
        continue
    if len(array1[-1]) == 12:
        break

for linha in range(len(array1)):
    soma_coluna += array1[linha][C]

if T == 'S':
    print(f'{soma_coluna:.1f}')

elif T == 'M':
    print(f'{soma_coluna /12:.1f}')
