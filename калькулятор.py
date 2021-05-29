# 1 задание

# print("Ноль в качестве знака операции"
#       "\nзавершит работу программы")
# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")

# 2 задание

# a = 10
# b = 20
# c = 30
# A = a + b
# B = c - a
# C = a + b + c
# print(A, B, C)

# 3 задание

# a = int(input("enter num: "))
# print(a * 4)

# 4 задание

# sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
# sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
# sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
# sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')

# 5 задание

'''доделать'''

# 6 задание

# 1 \ 2 задание

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# for i in a:
#     if i > 5:
#         b.append(i)
# print(b)


# 2 \ 2 задание

# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# for i in digits:
#     print(i * 9)

# 3 \ 2 задание

# fruits = ('banana','stawberry','apple','orange','limon','ananas')
# print(fruits[:6:5])

# 4 \ 2 задание

# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
# b = set(spisok_1)
# c = set(spisok_2)
# a = b.difference(c)
# print(a)

# 5 \ 2 задание

# i = 0
# while i < 300:
#     print(i)
#     i+= 2

# 6 \ 2 задание

# i = 0
# while i < 3:
#     import random as rd
#     random_number = rd.randint(0,2)
#     a = input("введите число")
#     print(random_number)
#     i += 1
#     if random_number == a:
#         print("вы выиграли")
#     else:
#         print("вы проиграли")

# 7 \ 2 задание
a = input('введите слово из 6 букв!!! ')
b = tuple(a)
print(b)