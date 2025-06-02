def factorial(n):
    if n < 0:
        return 'Enter a positive number.'
    else:
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)

n = int(input('Enter a number: '))
print(f'Factorial: {factorial(n)}')