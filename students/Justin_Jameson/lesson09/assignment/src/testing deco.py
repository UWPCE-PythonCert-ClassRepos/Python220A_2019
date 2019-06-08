import logging
import functools

logging.basicConfig(filename='example.log', level=logging.DEBUG)

do_debug = input('Debug? Y/N: ')

def debug(func):
    """Print the function signature and return value"""
    if do_debug.lower() == 'y':
        @functools.wraps(func)
        def wrapper_debug(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            logging.debug(f"Calling {func.__name__}({signature})")
            value = func(*args, **kwargs)
            logging.info(f"{func.__name__!r} returned {value!r}")
            return value
        return wrapper_debug
    else:
        @functools.wraps(func)
        def debug_disabled(*args, **kwargs):
            # print("Debug has been disabled")
            returned_value = func(*args, **kwargs)
            return returned_value

        return debug_disabled


@debug
def some_function():
    return"Just a funciton"

print(some_function())