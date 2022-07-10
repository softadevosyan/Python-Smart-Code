# # CALCULATOR
# text = input('Enter the numbers-->')
# c = 0
# smb = ('+-*/')
# try:
#     for i in text:
#         if i in smb:
#             x = int(text[0:text.index(i)])
#             y = int(text[text.index(i) + 1:])
#             if i == '+':
#                 print(f'x + y = {x + y}')
#             elif i == '-':
#                 print(f'x - y = {x - y}')
#             elif i == '*':
#                 print(f'x * y = {x * y}')
#             elif i == '/':
#                 print(f'x / y = {x / y}')
# except ZeroDivisionError:
#     print("Can't divide on 0!")
# except:
#     print('Write numbers not letters!')

# PASSWORD
# char = '!@%$#*&'
# while True:
#     try:
#         char_count = 0
#         number_count = 0
#         password = input("Enter the password-->")
#         if len(password) < 8:
#             print('The password is not strong')
#             continue 
#     except:
#         if password[0].isupper():
#             for i in password:
#                 if i in char:
#                     char_count += 1
#                 elif i.isdigit():
#                     number_count += 1
#         else:            
#             print('The password is not strong')
#             continue
#     try:
#         if number_count >= 2 and char_count >= 2:
#             print(password, 'Strong Password')
#             break
#     except:
#         print('The password is not strong')
#         continue
