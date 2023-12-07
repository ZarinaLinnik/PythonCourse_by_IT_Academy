# 1. Write .
def reverse_str(string: str, counter=1, res=[]) -> str:
    """
    This recursive function returns a reversed string.
    :string: original str.
    :counter: int (uses as index for the list that is called 'res').
    :res: list.
    :return: reversed str.
    """
    if len(string) in (1, 0):
        return string
    if counter != len(string) - 1:
        counter += 1
        counter = reverse_str(string, counter)
    res.append(string[counter])
    counter = counter - 1
    if counter != 0:
        return counter
    else:
        res.append(string[0])
        res_str = ''.join(res)
        res.clear()
        return res_str


print(repr(reverse_str('')))
print(repr(reverse_str(' ')))
print(reverse_str('spy'))
print(reverse_str('wow'))
print(reverse_str('ZaRiNa'))
print(reverse_str('yes'))
print(reverse_str('123'))
