def func(x, *y, a = 0, b = 0):
    for i in x:
        a += 1
    for i in y:
        b += i
    return a, b
print(func('hello', 2, 3, 4))