def main(number):
    part_a = number & 0b11111111111111
    number >>= 14
    part_b = number & 0b1
    number >>= 1
    part_c = number & 0b1111111
    number >>= 7
    part_d = number & 0b1
    number >>= 1
    number <<= 14
    number |= part_a
    number <<= 7
    number |= part_c
    number <<= 1
    number |= part_d
    number <<= 1
    number |= part_b
    return hex(number)


#  _TESTS_  #
print(main(0x2c16cc61))            # = 0x2c18c2b5
print(main(0x67e56510))            # = 0x67ca212b
print(main(0x43e36324))            # = 0x43c6491b
print(main(0x55347375))            # = 0x5566eba1
print(main(0xc1830037))            # = 0xc1806e18
