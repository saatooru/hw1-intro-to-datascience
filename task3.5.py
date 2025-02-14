import time
def decorator_1(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"func call executed in {end_time - start_time:.6f} sec")
        return result
    return wrapper
