def fibonacci(nth: int, odd_num=1, even_num=2, odd_fib=0, even_fib=1) -> int:
    """
    The recursive function to find the Nth number in the Fibonacci sequence.
    nth: int,
    odd_num: int,
    even_num: int,
    odd_fib: int,
    even_fib: int.
    Return: int.
    """
    if odd_num == nth:
        return odd_fib
    elif even_num == nth:
        return even_fib
    else:
        odd_fib, even_fib = odd_fib + even_fib, even_fib + (odd_fib + even_fib)
        return fibonacci(nth, odd_num+2, even_num+2, odd_fib, even_fib)


print(fibonacci(1), 0)
print(fibonacci(3), 1)
print(fibonacci(5), 3)
print(fibonacci(6), 5)
print(fibonacci(8), 13)
print(fibonacci(9), 21)
