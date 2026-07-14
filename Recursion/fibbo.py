def fib(n):

    # fib(1) = 1 and fib(2) = 1
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
print(fib(9))