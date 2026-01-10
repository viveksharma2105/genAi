from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

@my_decorator
def greet():
    print("hello! Inside the function.")
    
greet()
print(greet.__name__)  # Output: wrapper(if not use @wraps else greet)
