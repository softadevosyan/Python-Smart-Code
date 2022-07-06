# 1. calculator
# def calculator(x, y):
#     return f'x + y = {x + y}, x - y = {x - y}, x * y = {x * y}, x / y = {x // y}'
# print(calculator(x = int(input('Enter the value of x-> ')), y = int(input('Enter the value of y-> '))))
# 2. Max of two numbers
# def numbers(x, y):
#     if x > y:
#         return f'{x} is max'
#     else:
#         return f'{y} is max'
# print(numbers(x = int(input('Enter the value of x-> ')), y = int(input('Enter the value of y-> '))))
# 3. Sum all numbers
# def numbers(*args):
#     return sum(args)
# print(numbers(3,343,32,65,8,3,1,9876,2345678))
# 4. Multiplies all numbers 
# def multiply(*num):
#     result = 1
#     for i in num:
#         result *= i
#     return result
# print(multiply(2,5,10))
# 5. 
# def myfunc(x, y, c1 = 0, c2 = 0):
#     for i in x:
#         c1 += 1
#     for i in y:
#         c2 += 1
#     return f"Letter's number is {c1}\nNumber's number is {c2}"
# print(myfunc(input('Enter any word-->'), input('Enter any number-->')))
# 6. You are given a program that takes all 3 
# passengers ages as inputs and inserts them in 
# a list. Complete the program so that If it 
# finds a value less than 16, it breaks the 
# loop and outputs "Too young! ".
# If the age requirement is satisfied, the 
# program outputs "Get ready!".
# age_list = []
# c = 0
# while c < 3:
#     age = int(input('Enter the age-->'))
#     if age > 16:
#         age_list.append(age)
#         c += 1
#     else:
#         print("Too young")  
#         break
# else:      
#     print("Get ready!")
# Упражнение 85. Вычисляем длину гипотенузы
# def myfunc(a, b, c):
#     if a < c and b < c:
#         print(f'c = {(a**2 + b **2)**0.5}')
#     else:
#         print('N/C')
#         return a,b,c
# print(myfunc(int(input('Enter the length of a')), int(input('Enter the length of b')), int(input('Enter the length of c'))))
# Упражнение 86. Плата за такси??
# minimal = 4
# additional = 0.25
# def func(x):
#     distance = x // 1000
#     total = distance * additional
#     total += minimal
#     return total
# print(func(x = float(input('Enter the km ov your ride->'))))
# Упражнение 88. Медиана трех значений
# def main(x,y,z):
#     if x > y:
#         if x < z:
#             median = x
#         elif y > z:
#             median = y
#         else:
#             median = z
#     else:
#         if x > z:
#             median = x
#         elif y < z:
#             median = y
#         else:
#             median = z
#     return f'The median is {median}'
# print(main(x = float(input("Input first number: ")),y = float(input("Input second number: ")),z = float(input("Input third number: "))))
# Упражнение 98. Простое число??
# def main(x):
#     if x % x == 0 and x % 1 == x:
#         print('true')
#         return x
#     else:
#         print('false')
#         return x
# print(main(int(input('Enter an integer->>'))))
