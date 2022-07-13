# import random
# # def func(s:str='') -> str:
# #     for _ in range(random.randint(7,11)):
# #         s += chr(random.randint(33,126))
# #     return s
# print(func())

# Ex 2
# read = int(input('Enter the number of the line->'))
# with open('new.txt', 'rt') as f:
#     x = f.readlines()
# print(x[:read])
# Ex 3
# read = input('Enter the an animal->')
# with open('new.txt', 'r') as f:
#     x = f.readlines()
# x.append(read)
# with open('new.txt', 'a') as y:
#     y.write(f'\n{read}')
# Ex 4
# with open('new.txt', 'r') as x:
#     res = x.readlines()
# res.sort(key = len)
# print(res[-1])
# Ex 5 ??
# with open('new.txt', 'r') as x:
#     res = x.readlines()
# for i in res:
#     for j in i:
#         if j.isdigit() == True:
#             print(f'{j},', end = '')
# Ex 6
# with open('text.txt' , 'w') as file: 
#     password = input('Write a password') 
# print(file.write(password))


# 149 ??
# lineNum = 10
# with open('new.txt', 'rt') as x:
#     f = x.readlines()[:lineNum]
# print(f)
# 152??
# with open('new.txt') as myfile:
#     total_lines = sum(1 for line in myfile)
# print(total_lines)
# 153
# with open('new.txt', 'r') as x:
#     res = x.readlines()
# res.sort(key = len)
# print(res[-1])
# 158??
# with open('new.txt', 'r') as x:
#     print(x.read())
#     for i in x:
#         if i[0] == '#':
#             new = i.pop('#')
#             print(new)



    


