def positional(a, b, c):
    print(a, b, c)

def keyword(a='carrot', b='apple', c='banana'):
    print(a, b, c)

# 1
positional('apple', 'banana', 'carrot')
keyword('apple', 'banana', 'carrot')

# 2
try:
    positional()
except Exception as e:print(e)

keyword()