# 181 ??
# def func(total,coin):
#     penny = 0.01
#     nickel = 0.05
#     dime = 0.1
#     quarter = 0.25
#     if coin * penny == total and coin * nickel == total and coin * dime == total  and coin * quarter == total:
#         return True
#     else:
#         return penny * func(total,coin) or nickel * func(total,coin) or dime * func(total,coin) or quarter * func(total,coin) 
# print(func(1,0.3))

# ---------------------------------------------------------

# 182???
# from periodic import element





# Exercise 184: Flatten a List???
# def func(data):
#     if data == []:
#         return []
#     if type(data[0]) == list:
#         return func(data[0]) + func(data[1:])
#     return [data[0] + func(data[1:])]
# print(func([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))