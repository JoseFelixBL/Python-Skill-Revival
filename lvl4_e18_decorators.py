"""
Decorators
    Write a decorator `timer` that measures the time a function takes to 
    execute and prints it.
    Write a decorator `logger` that logs the arguments a function was called 
    with and its return value.
"""
"""
Example decorator definition:

    import functools

    def new_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Do  things
            result = func(*args, **kwargs)
            # Do other things
            return result
        return wrapper

"""
import functools
import time
import logging

logging.basicConfig(filename='lvl4_e18.log', encoding='utf-8', level=logging.INFO)


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"{args=} - {kwargs} - {result=}")
        return result
    return wrapper

def timer(func):
    """
    Decorator to measure the time a function takes to execute and print it
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_t = time.perf_counter()
        result = func(*args, **kwargs)
        stop_t = time.perf_counter()
        print(f"Time elapsed: {stop_t - start_t}")
        return result
    return wrapper

@timer
@logger
def count_many(end_num):
    """
    for loop with time waiting just to test
    """
    for _ in range(end_num):
        time.sleep(0.1)
    return "Good bye!"
count_many(15)