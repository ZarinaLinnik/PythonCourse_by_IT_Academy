def pow_num(num: int, power: int, mult=1) -> int:
    """
    The recursive function to calculate the power of a given number.
    num: int,
    power: int,
    mult: int.
    Return: int.
    """
    if power == 0:
        return mult
    else:
        mult *= num
        return pow_num(num, power-1, mult)


print(pow_num(4, 4), 256)
print(pow_num(3, 3), 27)
print(pow_num(2, 2), 4)
print(pow_num(1, 1), 1)
print(pow_num(0, 0), 1)
