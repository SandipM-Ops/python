import time

def timer(function):
    def wrapper(*args, **kwargs):
        start= time.time()
        result=function(*args, **kwargs)
        end= time.time()
        print(f"{function.__name__} ran in {end-start} time")
        return result
    return wrapper #return function defination

@timer
def example_fn(n):
    time.sleep(n)

example_fn(2)  
          