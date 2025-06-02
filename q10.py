l = input('Enter a letter: ')

if l.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f'{l} is vowel.')
else:
    print(f'{l} is consonant.')