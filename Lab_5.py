n = 0
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(1, 10):
            if c == a:
                for d in range(0, 10):
                    if d == b:
                        n += 1
                        s = 1000*a+100*b+10*c+d
                        print(s)
print('\nКількість чисел:', n)
