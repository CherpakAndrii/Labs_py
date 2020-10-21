from math import *

a = float(input('Введіть сторону a:'))
b = float(input('Введіть сторону b:'))
c = float(input('Введіть сторону c:'))
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
