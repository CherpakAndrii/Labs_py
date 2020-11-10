import re

s = 1
b = 1
x = input('x = ')
n = input('n = ')
if re.match(r'^-?[0-9]+\.?[0-9]*$', x) and n.isdigit():
    n = int(n)
    x = float(x)
else:
    print('Invalid input!')
    quit()
for i in range(1, n):
    a = b*x/i
    s += a
    b = a
else:
    print('s =', s)
