X = int(input())

for divisor in range(1, X + 1):
    if X % divisor == 0:
        print(divisor)
        