# ============================================================
# DECORATORS IN PYTHON
# Senior tip: A decorator is just a function that wraps another function
# to add behaviour before/after it — without touching the original code.
# ============================================================


# ============================================================
print("=" * 50)
print("1. What is a decorator? (plain function version first)")
print("=" * 50)
# ============================================================

# Before decorators, you'd manually wrap functions like this:
def greet():
    print("Hello!")

def manual_border(func):
    def wrapper():
        print("--- start ---")
        func()
        print("--- end ---")
    return wrapper

greet_with_border = manual_border(greet)
greet_with_border()


# ============================================================
print("\n" + "=" * 50)
print("2. The @ syntax — cleaner way to wrap")
print("=" * 50)
# ============================================================

# @add_border is just shorthand for: say_hi = add_border(say_hi)
def add_border(func):
    def wrapper():
        print("--- start ---")
        func()
        print("--- end ---")
    return wrapper

@add_border
def say_hi():
    print("Hi there!")

say_hi()


# ============================================================
print("\n" + "=" * 50)
print("3. Decorator with arguments (*args, **kwargs)")
print("=" * 50)
# ============================================================

# Senior tip: your wrapper must accept and pass through ALL arguments,
# otherwise the decorator will break any function with params.

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(3, 5)
greet_user("Kishan", greeting="Hey")


# ============================================================
print("\n" + "=" * 50)
print("4. Real-world use case: timing a function")
print("=" * 50)
# ============================================================

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start):.4f}s")
        return result
    return wrapper

@timer
def slow_task():
    time.sleep(0.1)
    print("Task done.")

slow_task()


# ============================================================
print("\n" + "=" * 50)
print("5. Real-world use case: access control / auth check")
print("=" * 50)
# ============================================================

def require_auth(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_logged_in"):
            print("Access denied. Please log in.")
            return
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def view_dashboard(user):
    print(f"Welcome to dashboard, {user['name']}!")

guest = {"name": "Guest", "is_logged_in": False}
admin = {"name": "Kishan", "is_logged_in": True}

view_dashboard(guest)   # blocked
view_dashboard(admin)   # allowed


# ============================================================
print("\n" + "=" * 50)
print("6. Stacking multiple decorators")
print("=" * 50)
# ============================================================

# Senior tip: decorators apply bottom-up.
# @A @B def f()  is the same as  f = A(B(f))
# So B wraps f first, then A wraps the result.

def bold(func):
    def wrapper(*args, **kwargs):
        return "**" + func(*args, **kwargs) + "**"
    return wrapper

def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@bold         # applied second (outer)
@uppercase    # applied first (inner)
def message():
    return "hello"

print(message())   # **HELLO**


# ============================================================
print("\n" + "=" * 50)
print("7. functools.wraps — preserve the original function name")
print("=" * 50)
# ============================================================

# Senior tip: without @wraps, debugging becomes painful.
# The wrapped function loses its __name__ and __doc__.

from functools import wraps

def my_decorator(func):
    @wraps(func)            # copies __name__, __doc__ from func to wrapper
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def important_function():
    """This does something important."""
    pass

print(important_function.__name__)  # important_function  ✓  (without @wraps it'd be 'wrapper')
print(important_function.__doc__)   # This does something important.


# ============================================================
print("\n" + "=" * 50)
print("8. Class-based decorator")
print("=" * 50)
# ============================================================

# Senior tip: use a class decorator when you need to track state across calls.

class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):   # makes the instance callable
        self.count += 1
        print(f"[Call #{self.count}] {self.func.__name__}")
        return self.func(*args, **kwargs)

@CallCounter
def fetch_data():
    print("Fetching...")

fetch_data()
fetch_data()
fetch_data()
print(f"Total calls: {fetch_data.count}")
