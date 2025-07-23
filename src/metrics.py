import time

def time_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = round(time.time() - start, 2)
        print(f"⏱️ Function '{func.__name__}' ran in {duration}s")
        return result
    return wrapper
