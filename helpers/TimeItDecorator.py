import functools
import time


def timeit_decorator(method):
    @functools.wraps(method)
    def timed(*args, **kwargs):
        start_time = time.perf_counter()
        result = method(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"{method.__name__} took {elapsed_time:.6f} seconds to execute")
        return result

    return timed
