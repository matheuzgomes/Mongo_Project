from functools import wraps
import time


def benchmark(func):
    '''Benchmark My Controller'''
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        end = time.perf_counter()
        response = end - start
        print(f"Time elapsed in {func.__name__} was {response:.4f} seconds")
        return result

    return wrapper
