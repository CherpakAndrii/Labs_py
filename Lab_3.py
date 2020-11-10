x = 0.56
n = 0
s = 0
b = 1
while abs(b) > 10**(-4):
    s += b
    n += 1
    b = (-1)**n * (x**(2 * n) + 1)/(2**n + 1)
print('The sum of the series =', s)
