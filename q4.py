sums = 0
while True:
    x = input('Enter a number: ')
    if x:
        sums += int(x)
    else: break
print(f'Sum of digits: {sums}')