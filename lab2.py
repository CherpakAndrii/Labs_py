import os, re
a, b, c, numList = 'a', 'b', 'c', []


for n in a, b, c:
    n = input('{} = '.format(n))
    if re.match(r"^-?[0-9]+\.?[0-9]*$", n):
        n = float(n)
        if n not in numList:
            numList.append(n)
        else:
            print('\nСеред чисел є рівні')
            os.system('pause')
            quit()
    else:
        print('Введено нечислове значення!')
        quit()
print('\nСеред заданих чисел немає однакових')
os.system('pause')
