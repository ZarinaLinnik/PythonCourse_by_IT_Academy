def palindrome(string: str, st=0, end=0) -> bool:
    """
    The recursive function checks a given string is a palindrome.
    string: str.
    st: int.
    end: int.
    return: bool.
    """
    end = len(string) - 1
    if len(string) in (1, 0):
        return True
    if st + 1 > len(string) // 2:
        return True
    if string[st] == string[end]:
        return palindrome(string, st+1, end-1)
    else:
        return False


print(palindrome(''))
print(palindrome('k'))
print(palindrome('wow'))
print(palindrome('key'))
print(palindrome('wdfhjfdw'))