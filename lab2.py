import re
a, b, c, d = 'a', 'b', 'c', 'd'

def check(n):
    n = input('{} = '.format(n))
    if re.match(r"^[0-9]+\.?[0-9]*$", n):
        n = float(n)
    else:
        print('Invalid input')
        quit()

check(a)
check(b)
check(c)
check(d)
if a<=c and b<=d or a<=d and b<=c:
    s = ''
else:
    s = 'не '
print('Прямокутник зі сторонами a, b {}можна розмістити всередині прямкутника зі сторонами c, d.'.format(s))
