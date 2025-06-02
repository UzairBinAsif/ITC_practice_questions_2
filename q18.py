def func(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    try:
        print(round(a/b, 3))
    except ZeroDivisionError as z:
        print(z)

func(2, 3)
    