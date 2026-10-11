import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"Time: {end - start:.6f} seconds")
        return result

    return wrapper


@timer
def work():
    return sum(range(100_000))


print(work())