class A(object):
    bar = 1


def fib(n):
    if n <= 1:
        return 1
    result = fib(n-1) + fib(n-2)
    return result


def decorator(func):
    x = 10
    def inner(*args, **kwargs):
        print(x)
        return func(*args, **kwargs)
    return inner


x = 1
