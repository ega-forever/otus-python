from functools import wraps

STEP_KEY = '__step__'


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        kwargs.update({STEP_KEY: kwargs.get(STEP_KEY) + 1 if isinstance(kwargs.get(STEP_KEY), int) else 0})
        delimiters = str.join("", list(map(lambda _: "____", range(kwargs.get(STEP_KEY)))))
        print(f'{delimiters}--> {func.__name__}({args[0]})')
        res = func(*args, **kwargs)
        print(f'{delimiters}<-- {func.__name__}({args[0]})')
        return res

    return wrapper


@trace
def fib(times=1, *args, **kwargs):
    last_number, last_last_number = args if len(args) == 2 else list([1, 0])
    if times == 0:
        return last_number
    return fib(times - 1, last_number + last_last_number, last_number, **kwargs)


if __name__ == '__main__':
    print(fib(3))
