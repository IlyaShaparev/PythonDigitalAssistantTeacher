from math import log, tan


def main(y):
    if y < 177:
        return 56 * (98 + 95 * y ** 3 + y / 51) ** 4 - 77 * (84 * y) ** 7 - 1
    elif 177 <= y < 189:
        return y ** 2
    elif 189 <= y < 224:
        return 50 + y / 28 + y ** 3 / 28 + 9 * (log(y ** 2 + y ** 3)) ** 2
    elif 224 <= y < 312:
        return 30 * (15 * y + 36 * y ** 2 + 1) ** 4
    elif y >= 312:
        return 27 * (80 * y ** 3 - y ** 2 - 1) ** 3 + tan(y)


print(main(270))            # = 1.43e+27
print(main(119))            # = 3.68e+34
print(main(277))            # = 1.76e+27
print(main(248))            # = 7.26e+26
print(main(275))            # = 1.66e+27
