def main(m, a, n):
    summ = 0
    for j in range(1, n + 1):
        for k in range(1, a + 1):
            for i in range(1, m + 1):
                summ += i ** 7
                summ += (k ** 3 + 49 * j ** 2 + 83) / 90
                summ += abs(j) ** 5
    return summ


print(main(5, 4, 2))            # = 7.75e+05
print(main(3, 7, 3))            # = 5.47e+04
print(main(4, 3, 5))            # = 3.34e+05
print(main(6, 7, 2))            # = 5.28e+06
print(main(4, 5, 8))            # = 1.99e+06
