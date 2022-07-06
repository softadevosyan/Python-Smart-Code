# Exercise 173: Total the Value
# def myfunc():
#     x = input('enter a num->')
#     if x == '':
#         return 0
#     return int(x) + myfunc()
# print(myfunc())


# ---------------------------------------



# Exercise 174: Greatest Common Divisor
# def func(a,b):
#     if b == 0:
#         return a
#     return func(b, a % b)
# print(func(12,54))

# ---------------------------------------


# Exercise 178: Recursive Palindrome
# def polid(text):
#     if text == text[::-1]:
#         return True
#     if text[0] != text[-1]:
#         return False
#     return polid(text[1:-1])
# print(polid(text = str(input('Enter the word -> '))))


# ---------------------------------------


# Exercise 180: String Edit Distance
# def func(s,t):
#     if len(s) == 0:
#         return len(t)
#     elif len(t) == 0:
#         return len(s)
#     else:
#         cost = 0
#         if s[-1] != t[-1]:
#             cost = 1
#         d1 = func(s[:-1], t) + 1
#         d2 = func(s, t[:-1]) + 1
#         d3 = func(s[:-1], t[:-1]) + cost
#         return min(d1, d2, d3)
# print(func(s = str(input('enter a text->')), t = str(input('enter a text->'))))    

# ---------------------------------------


# Exercise 184: Flatten a List???
# def func(data):
#     if data == []:
#         return []
#     if type(data[0]) == list:
#         return func(data[0]) + func(data[1:])
#     return [data[0] + func(data[1:])]
# print(func([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))