def log_call(func):
    def wrapper(*args, **kwargs):
        print("Function called:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log_call
def multiply(a, b):
    return a * b


print(multiply(5, 4))