from functools import wraps
import time


def timer(func):
    """Decorator function to calculate the time of a function call """

    @wraps(func)
    def timedcalls(*args):
        """Call function with args; return time in seconds and result"""
        t0 = time.clock()
        result = func(*args)
        t1 = time.clock()
        return t1-t0, result
    return timedcalls


def memoize(func):
    """Decorator function to memoizes the returned values of the functions
       that is being decorated
    """

    # cache to store the results of the computation
    cache = dict()

    @wraps(func)
    def memcached(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memcached


@timer
@memoize
def fib(num):
    "calculates the fibonacci number of input num"

    a, b = 1, 1
    for i in range(num - 1):
        a, b = b, a+b
    return a

if __name__ == "__main__":
    print fib(100)
    print fib(20)
    print fib(30)
    print fib(100)
