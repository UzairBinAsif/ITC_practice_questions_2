def func(n):
    if n < 0:
        return 'Enter a positive number'
    if n == 0 or n == 1:
        return 'not prime'
    if n == 2:
        return 'prime'
    for i in range(2, int(1e3)):
        if i==n:
            continue
        if n%i==0:
            return 'not prime'
    return 'prime'
x = int(input('Enter a number: '))
print(func(x))