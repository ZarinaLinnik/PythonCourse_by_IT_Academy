# 5. Write a function that takes an ordered list of numbers without duplicates
# and returns a string with ranges for those numbers,
# check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"
# PS. Without concatenations
def range_numbers(list_numbers: list) -> str:
    """
    This function takes an ordered list of numbers without duplicates
    and returns a string with ranges for those numbers
    :parameter list_numbers: list.
    :returns: str.
    """
    res = []
    switch = 0
    for i in range(len(list_numbers) - 1):
        if i == len(list_numbers) - 2:
            if list_numbers[i] - 1 == list_numbers[i - 1] and list_numbers[i] + 1 == list_numbers[i + 1]:
                res.append(f'{num}-{list_numbers[i + 1]}')
            elif list_numbers[i] - 1 == list_numbers[i - 1] and list_numbers[i] + 1 != list_numbers[i + 1]:
                res.append(f'{num}-{list_numbers[i]}, {list_numbers[i+1]}')
            elif list_numbers[i] + 1 == list_numbers[i + 1]:
                res.append(f'{list_numbers[i]}-{list_numbers[i + 1]}')
            else:
                res.append(f'{list_numbers[i]}, {list_numbers[i + 1]}')
            break

        if list_numbers[i] + 1 == list_numbers[i + 1]:
            if switch == 0:
                num = list_numbers[i]
                switch = 1
        else:
            if i != 0:
                if list_numbers[i] - 1 == list_numbers[i - 1]:
                    res.append(f'{num}-{list_numbers[i]},')
                    switch = 0
                else:
                    res.append(f'{list_numbers[i]},')
            if i == 0:
                res.append(f'{list_numbers[i]},')

    res = ' '.join(res)
    return res


print(range_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(range_numbers([0, 1, 2, 3, 4, 7, 8, 10]))
print(range_numbers([4, 7, 10]))
print(range_numbers([2, 3, 8, 9]))
