n = int(input('Enter a number: '))

if n <= 0:
    print('Error: Enter a positive number.')
else:
    x=0
    y=1
    if n >= 1:
        print(x, end=', ')
    if n >= 2:
        print(y, end=', ')
    if n >= 3:
        for i in range(3, n+1):
            result = x+y
            print(result, end=', ')
            x=y
            y=result