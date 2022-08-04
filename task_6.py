def main(keys):
    dict_1 = {'VUE': 0,
              'GN': 1,
              'MAX': 2}
    dict_2 = {'VUE': 3,
              'GN': 4,
              'MAX': 5}
    dict_3 = {'VUE': 6,
              'GN': 7,
              'MAX': 8}
    dict_4 = {1960: dict_1,
              1990: dict_2}

    if keys[1] == 1979:
        return dict_4[keys[0]][keys[2]]
    else:
        if keys[0] == 1990:
            return 9
        else:
            return dict_3[keys[2]]


# _TESTS_ #
print(main([1990, 2008, 'VUE', 'OPA']))            # = 9
print(main([1990, 1979, 'GN', 'OPA']))             # = 4
print(main([1960, 2008, 'GN', 'UNO']))             # = 7
print(main([1990, 1979, 'MAX', 'UNO']))            # = 5
print(main([1960, 1979, 'GN', 'UNO']))             # = 1
