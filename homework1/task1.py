import time
from enum import Enum
from functools import wraps


def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f'processed function {func.__name__} in {time.time() - start}ms')
        return res
    return wrapper

@time_decorator
def pow_numbers(numbers, powed=2):
    powed_numbers = []
    for number in numbers:
        powed_numbers.append(number ** powed)
    return powed_numbers

class FilterType(Enum):
     ODD = 1
     EVEN = 2
     PRIME = 3


def is_prime(n):

    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

@time_decorator
def filter_numbers(numbers, filter_by = FilterType.ODD):

    if filter_by == FilterType.ODD:
        def filter_func(n):
            if n % 2 != 0:
                return n
        return list(filter(filter_func, numbers))

    if filter_by == FilterType.EVEN:
        def filter_func(n):
            if n % 2 == 0:
                return n
        return list(filter(filter_func, numbers))

    if filter_by == FilterType.PRIME:
        def filter_func(n):
            if is_prime(n):
                return n
        return list(filter(filter_func, numbers))

if __name__ == '__main__':
    print(f'powed_number[1, 2, 3]: {pow_numbers([1, 2, 3], powed=3)}')
    print(f'filtered odd numbers from [1, 4, 5, 11, 15]: {filter_numbers([1, 4, 5, 11, 15], filter_by=FilterType.ODD)}')
    print(f'filtered even numbers from [1, 4, 5, 11, 15]: {filter_numbers([1, 4, 5, 11, 15], filter_by=FilterType.EVEN)}')
    print(f'filtered prime numbers from [1, 4, 5, 11, 15]: {filter_numbers([1, 4, 5, 11, 15], filter_by=FilterType.PRIME)}')
