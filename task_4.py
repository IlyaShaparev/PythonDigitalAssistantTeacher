from math import log2, atan


def main(n):
    if n == 0:
        return 0.93
    elif n == 1:
        return 0.29
    else:
        return (atan(43 * (main(n-1)) ** 3 - 1 - 15 * (main(n-2)) ** 2))/77 + log2(main(n-2)) ** 2 + 1


print(main(6))          # = 1.02e+00
print(main(4))          # = 1.02e+00
print(main(7))          # = 6.74e+00
print(main(9))          # = 8.56e+00
print(main(3))          # = 4.21e+00
