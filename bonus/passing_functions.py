# quick sample to demonstrate the difference between pass func vs func()


def wrapper_func(func):
    print("doing some wrapper action")
    if func is not None:
        print("running func")
        func()


def some_action():
    print("doing some action")


wrapper_func(some_action)

print("-" * 20)

wrapper_func(some_action())
