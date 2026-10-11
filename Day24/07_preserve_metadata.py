from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def greet():
    """Display a greeting."""
    print("Hello!")


greet()
print(greet.__name__)
print(greet.__doc__)