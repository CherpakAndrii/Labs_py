import math
eps, x1, x2, x3 = 0.00001, 0.818, 1.403, 3.141


def get_area_1(x_min, x_max):
    s = 0
    x = x_min
    while x<=x_max:
        a = math.log(1+x**2)
        b = math.e**(-1*x**2)
        s += (a-b) * eps
        x+=eps
    return s


def get_area_2(x_min, x_max):
    s = 0
    x = x_min
    while x<=x_max:
        c = 2/x*math.cos(x/2)
        b = math.e**(-1*x**2)
        s += (c - b) * eps
        x+=eps
    return s


area = get_area_1(x1, x2) + get_area_2(x2, x3)
print('The area of the figure limited by these functions: ', area)
