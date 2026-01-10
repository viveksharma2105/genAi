from functools  import wraps
def log_activity(fun):
    @wraps(fun)
    def wrapper(*args,**kwargs):
        print(f"calling: {fun.__name__}")
        result = fun(*args,**kwargs)
        print(f"finished: {fun.__name__}")
        return result
    return wrapper
        
@log_activity
def add(x, y):
    print(f"Adding {x} and {y}")
    
add(3, 5)