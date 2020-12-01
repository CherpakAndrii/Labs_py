import math
# import numpy as np
eps = 0.00001
x1 = 0.818
x2 = 1.403
x3 = 3.141
a = 'math.log(1+x**2)'
b = 'math.e**(-1*x**2)'
c = '2/x*math.cos(x/2)'


def get_area(x_min, x_max, f1, f2):
    s = 0
    # for x in np.arrange(x_min, x_max, eps):
    #     s += (eval(f1)-eval(f2))*eps
    x = x_min
    while x<=x_max:
        s += (eval(f1) - eval(f2)) * eps
        x+=eps
    return s


area = get_area(x1, x2, a, b) + get_area(x2, x3, c, b)
print('The area of the figure limited by these functions: ', area)
