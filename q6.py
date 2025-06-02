x = int(input('\nEnter a number to find factorial: '))
fact = 1
for i in range(x, 0, -1):
    fact *= i
print(f'factorial: {fact}')