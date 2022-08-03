from math import log


def main(n):
    if n == 0:
        return -0.02
    elif n == 1:
        return -0.6
    else:
        return 96 * (log((main(n - 1)) ** 2 + (main(n - 2)) ** 3)) ** 2 + 1


print(main(2))          # = 1.01e+02
print(main(9))          # = 1.16e+05
print(main(8))          # = 1.13e+05
print(main(3))          # = 8.19e+03
print(main(4))          # = 3.12e+04
