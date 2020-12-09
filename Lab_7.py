from random import randint
while True:
    n = int(input('Введіть кількість елементів: '))
    if n%2 == 0:
        break
    print('Кількість членів повинна бути кратна 2\n')


def get_list(num):
    lst = []
    while len(lst)<num:
        a = randint(1, num**2)
        if a not in lst:
            lst.append(a)
    return lst

list1 = get_list(n)
print('Згенерований список:', list1)
list2 = [0]*n
list1.sort(reverse=True)
for i in range(0, int(n/2)):
    list2[i] = list1[2*i]
    list2[-(i+1)] = list1[2 * i + 1]
    if sum(list2[:int(n/2)])>sum(list2[int(n/2):]):
        list2.reverse()
print('Список, що найбільше задовольняє умову: ', list2)


# def l_reverse(lst):
#     lst1 = []
#     for a in range(1, len(lst)+1):
#         lst1.append(lst[-a])
#     return lst1
