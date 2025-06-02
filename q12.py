x = int(input('Enter a number: '))
if (x%3 or x%5) == 0:
    print(f'{x} is divisible by 3 and 5 both.')
else:
    print(f'{x} is not divisible by 3 and 5 both.')