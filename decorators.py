import functools
import time


def timer(func):
    """Print the runtime of the decorated function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} secs.')
        return value
    return wrapper


@timer
def add_n(n: int):
    result = 0
    for i in range(n):
        result += i
    return result


print('Result:', add_n(300000))
