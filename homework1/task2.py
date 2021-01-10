from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        STEP_KEY = '__step__'
        kwargs.update({STEP_KEY: kwargs.get(STEP_KEY) + 1 if isinstance(kwargs.get(STEP_KEY), int) else 0})
        delimiters = str.join("", list(map(lambda _: "____", range(kwargs.get(STEP_KEY)))))
        print(f'{delimiters}--> {func.__name__}({args[0]})')
        res = func(*args, **kwargs)
        print(f'{delimiters}<-- {func.__name__}({args[0]})')
        return res

    return wrapper


@trace
def fib(times=1, *args, **kwargs):
    lastNumber, lastLastNumber = args if len(args) == 2 else list([1, 0])
    if times == 0:
        return lastNumber
    return fib(times - 1, lastNumber + lastLastNumber, lastNumber, **kwargs)


print(fib(3))
