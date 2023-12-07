import time

class Timing:
    def timed(function):
        def wrapper(*args, **kwargs):
            before = time.perf_counter()
            func_value = function(*args, **kwargs)
            after = time.perf_counter()
            total_time = after - before
            res = '{0:.10f}'.format(total_time)
            print(f"{function.__name__} took {res}s")
            return func_value
        return wrapper
    
    # @timed
    def __init__(self):
        print("Hello World!")

    @timed
    def __str__(self):
        return "yo is me"
    

if __name__ == "__main__":
    t1 = Timing()
    print(t1)