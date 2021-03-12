"""
Advanced Decorators
Instructions
Create a logging_decorator() which is going to log the name of the
function that was called, the arguments it was given and finally the
returned output.

Expected Output
https://cdn.fs.teachablecdn.com/jA2ypes2RfuB0cuC41yd

HINT 1: You can use function.__name__ to get the name of the function.

HINT 2: You'll need to use *args

SOLUTION: https://repl.it/@appbre
"""


def logging_decorator(f):
    def wrapper(*args, **kwargs):
        arg_str = ""
        if len(args) > 0:
            arg_str += ", ".join([str(a) for a in args])
        if len(args) > 0 and len(kwargs) > 0:
            arg_str += ", "
        if len(kwargs) > 0:
            arg_str += ", ".join([f"{k}:{v}" for k, v in kwargs.items()])
        print(f"you called {f.__name__}({arg_str})")
        print(f"It returned: {f(*args, **kwargs)}")

    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a + b + c


a_function(1, 2, 3)

a_function(1, c=2, b=3)
