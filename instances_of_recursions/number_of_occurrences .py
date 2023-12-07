def num_letter(symbol: str, string: str, index=0, counter=0) -> int:
    """
    This recursive function counts the number of occurrences of a given character in a string.
    symbol: str,
    string: str,
    index: int,
    counter: int.
    Return: int.
    """
    if index == len(string):
        return counter
    else:
        if string[index] == symbol:
            counter += 1
        return num_letter(symbol, string, index+1, counter)


print(num_letter('a', 'Alana'))
print(num_letter('b', 'bobb'))
print(num_letter('O', 'Olow'))
print(num_letter('4', '2344544'))
