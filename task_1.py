from math import floor


def main(z, x):
    summ = x ** 4
    summ -= 20 * (z / 67 + 16 * x ** 3) ** 5
    summ += 64 * (floor(59 * x ** 3 - 53 * z ** 2 - 1)) ** 7
    return summ


#  _TESTS_  #
print(main(-0.52, -0.46))           # = -1.60e+11
print(main(0.79, 0.83))             # = -1.29e+06
print(main(-0.31, -0.67))           # = -2.94e+11
print(main(-0.95, 0.07))            # = -4.34e+13
print(main(-0.35, 0.61))            # = 4.99e+06
