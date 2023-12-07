def count_lower_and_upper(string: str) -> tuple:
    """
    The function returns a number of lowercase letters and a number of uppercase letters.
    :parameter string: str.
    :return: tuple(num_lowercase_letters, num_uppercase_letters)
    """
    lowercase_letters = 0
    uppercase_letters = 0
    for i in string:
        if i.isalpha() and i.islower():
            lowercase_letters += 1
    for i in string:
        if i.isalpha() and i.isupper():
            uppercase_letters += 1
    return lowercase_letters, uppercase_letters


print(count_lower_and_upper(''))
print(count_lower_and_upper(' '))
print(count_lower_and_upper(','))
print('little', count_lower_and_upper('маленькие буквы'), len('маленькие буквы'))
print('BIG-1', count_lower_and_upper('БОЛЬШИЕ БУКВЫ'), len('БОЛЬШИЕ БУКВЫ'))
print('BIG-2', count_lower_and_upper('БОЛЬШИЕ_БУКВЫ_'), len('БОЛЬШИЕ_БУКВЫ_'))
print(count_lower_and_upper('Такой текст'), len('Такой текст'))
print(count_lower_and_upper('или ТаКоЙ бЫвАеТ'), len('или ТаКоЙ бЫвАеТ'))
