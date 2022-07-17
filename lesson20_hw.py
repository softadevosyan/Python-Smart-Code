# import json
# Ex 1
# list1 = ['Ani', 'Jessy', 'Ben'] 
# list2 = [1,2,3]
# mydict = {}
# for i,j in zip(list1,list2):
#     mydict[i] = j
# print(mydict)
# with open('mydict.txt','w') as f:
#     f.write(f'{mydict}')
# Ex 2
# lyrics = '''She, May be the face I can't forget
# A trace of pleasure or regret
# May be my treasure or the price I have to pay'''
# with open('lyrics.json', 'w') as f:
#     json.dump(lyrics, f)
# with open('lyrics.json') as x:
#     y = json.load(x)
# print(y)
# Ex 3
# def func(x, res, mylist):
#     for i in range(1,x):
#         if i % 3 == 0 or i % 5 == 0:
#             res += i
#             mylist.append(i)
#             y = f'Sum = {res}\nMultiples of {x} are {mylist}'
#     return y
# final = func(x = int(input('Enter a num-->')), res = 0, mylist = [])
# with open('new.json', 'w') as f:
#     json.dump(final, f)
# with open('new.json') as z:
#     res = json.load(z)
# print(res)
# print(final)
# Ex 4
# vowels = 'a,e,i,o,u,y'
# word = str(input('Enter a word-->'))
# c = 0
# for i in word:
#     if i in vowels:
#         c += 1
# res = f'The count of vowels in {word} is {c}'
# print(res) 
# with open('vowels.json', 'w') as f:
#     json.dump(res, f)
# Ex 5
# text = 'another pause and more eying and siding around each other'
# with open('text.txt', 'w') as f:
#     f.write(f'{text}')
# newdict = {}
# count_1 = 0
# count_2 = 0
# with open('text.txt', 'rt')as x:
#     t = x.read()
#     t = t.split(' ')
# print(t)
# for i in t:
#     if i == 'another':
#         count_1 += 1
#     elif i == 'and':
#         count_2 += 1
# newdict['another'] = count_1
# newdict['and'] = count_2
# print(newdict)
# Ex 6
# mylist = ['a', 'b', 'a', 'c', 'b']
# newlist = []
# for i in mylist:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)
# Ex 7
# text = '''London is a famous and historic city. It is the capital of England in the United Kingdom. The city is quite popular for international tourism because London is home to one of the oldest-standing monarchies in the western hemisphere. Rita and Joanne recently traveled to London. They were very excited for their trip because this was their first journey overseas from the United States.'''
# with open('word.txt', 'w') as f:
#     f.write(f'{text}')
# with open('word.txt', 'rt') as x:
#     res = x.read()
#     count_1 = 0
#     count_2 = 0
#     for i in res:
#         if i.isupper():
#             count_1 += 1
#         elif i.islower():
#             count_2 += 1
#     print(f'Upper is {count_1} \nLower is {count_2}')