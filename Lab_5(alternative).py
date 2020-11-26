# n = 0
# for i in range(10, 100):
#     n+=1
#     a = i*101
#     print(a)
# print('Кількість чисел: ', n)
#
#
# n = 0
# for i in range(10, 100):
#     n+=1
#     print(str(i)+str(i))
# print('\nКількість чисел: ', n)
#
#
#
# n = 0
# for i in range(1000, 10000):
#     if i//100 == i%100:
#         n += 1
#         print(i)
# print('\nКількість чисел: ', n)
#
#       #       #       #
#
# n = 0
# c = int(input('Введіть бажану кількість цифр в числі: '))
# if c % 2 == 0:
#     c = int(c/2)
#     for i in range(10**(c-1), 10**c):
#         print(i*((10**c)+1))
#         n += 1
#     print('\nКількість чисел:', n)
# else: print('кількість цифр має бути парною!')
#
#
#
# n = 0
# c = int(input('Введіть бажану кількість цифр в числі: '))
# if c % 2 == 0:
#     c = int(c/2)
#     for i in range(10**(c-1), 10**c):
#         print(str(i)*2)
#         n += 1
#     print('\nКількість чисел:', n)
# else: print('кількість цифр має бути парною!')
#
#
#
# n = 0
# c = int(input('Введіть бажану кількість цифр в числі: '))
# if c % 2 == 0:
#     for i in range(10**(c-1), 10**c):
#         if i//10**(c/2) == i % 10**(c/2):
#             print(i)
#             n += 1
#     print('\nКількість чисел:', n)
#
#
#
#   #   #      #      #
#
#
# count, lst, handle = 0, [], open('a.txt')
# for line in handle:
#     numbers = line.split(' ')
#     for num in numbers:
#         num = num.strip(',')
#         if num.isdigit():
#             lst.append(num)
# for obj in lst:
#     if len(obj) % 2 == 0 and obj[:int(len(obj)/2)] == obj[int(len(obj)/2):]:
#         count += 1
#         print(obj)
# print('\nКількість чисел, що відповідають умові:', count, 'із', len(lst))
