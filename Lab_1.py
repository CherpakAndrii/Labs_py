import math, re
a, b, c = 'a', 'b', 'c'

for n in a, b, c:
    n = input('Введіть сторону {}'.format(n))
    if re.match(r"^[0-9]+\.?[0-9]*$", n):
        n = float(n)
    else:
        print('Введено некоректне значення!')
        quit()

if a + b > c and b + c > a and a + c > b and a > 0 and b > 0 and c > 0:
    p = (a + b + c)/2
    S = sqrt(p*(p-a)*(p-b)*(p-c))
    r = S/p
    R = a*b*c/(4*S)
    bisA = sqrt(b*c*(a+b+c)*(b+c-a))/(b+c)
    bisB = sqrt(a*c*(a+b+c)*(a+c-b))/(a+c)
    bisC = sqrt(a*b*(a+b+c)*(a+b-c))/(a+b)
    print('')
    print('Бісектриса кута А дорівнює', round(bisA, 2))
    print('Бісектриса кута B дорівнює', round(bisB, 2))
    print('Бісектриса кута C дорівнює', round(bisC, 2))
    print('Радіус вписаного кола:', round(r, 2))
    print('Радіус описаного кола:', round(R, 2))
else:
    print('Заданого трикутника не існує')
