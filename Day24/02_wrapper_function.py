def login_required(func):
    def wrapper():
        print("Checking login...")
        func()
    return wrapper


@login_required
def dashboard():
    print("Welcome to dashboard")


dashboard()