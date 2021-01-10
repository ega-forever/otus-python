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
def powNumbers(numbers, powed=2):
    powedNumbers = []
    for n in numbers:
        powedNumbers.append(n ** powed)
    return powedNumbers


print(f'powedNumber[1, 2, 3]: {powNumbers([1, 2, 3], powed=3)}')

class FilterType(Enum):
     ODD = 1
     EVEN = 2
     PRIME = 3


def isPrime(n):

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
def filterNumbers(numbers, filterBy = FilterType.ODD):

    if filterBy == FilterType.ODD:
        def filterFunc(n):
            if n % 2 != 0:
                return n
        return list(filter(filterFunc, numbers))

    if filterBy == FilterType.EVEN:
        def filterFunc(n):
            if n % 2 == 0:
                return n
        return list(filter(filterFunc, numbers))

    if filterBy == FilterType.PRIME:
        def filterFunc(n):
            if isPrime(n):
                return n
        return list(filter(filterFunc, numbers))

print(f'filtered odd numbers from [1, 4, 5, 11, 15]: {filterNumbers([1, 4, 5, 11, 15], filterBy=FilterType.ODD)}')
print(f'filtered even numbers from [1, 4, 5, 11, 15]: {filterNumbers([1, 4, 5, 11, 15], filterBy=FilterType.EVEN)}')
print(f'filtered prime numbers from [1, 4, 5, 11, 15]: {filterNumbers([1, 4, 5, 11, 15], filterBy=FilterType.PRIME)}')
