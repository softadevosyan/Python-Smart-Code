def func(x, *y, res = 0):
    for i in x, y:
        res += 1
        summ = sum(y)
    return res
print(func('hello', 2, 3, 4))