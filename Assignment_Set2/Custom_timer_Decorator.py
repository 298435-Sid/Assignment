import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Function '{func.__name__}' took {end - start:.4f} seconds to run.")
    return wrapper

@timer
def waste_time():
    time.sleep(1.5)

waste_time()