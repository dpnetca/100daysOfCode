# def outer_function():
#     print("outer")

#     def inner_function():
#         print("inner")

#     inner_function()


# outer_function()
# # RESULT:
# # outer
# # inner


# inner_function()
# # RESULT:
# # NameError: name 'inner_function' is not defined


# def outer_function():
#     print("outer")

#     def inner_function():
#         print("inner")

#     return inner_function


# inner_function = outer_function()
# # RESULT:
# # outer

# inner_function()
# # RESULT:
# # inner

import time


def delay_decorator(function):
    def wrapper_function():
        # do something before function
        time.sleep(2)
        function()
        # or do something after function

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


def say_bye():
    print("Bye")


say_hello()

# @ is syntactic sugar, same result can be done via:
decorated_function = delay_decorator(say_bye)
decorated_function()
